"""The met_eireann component."""
from datetime import timedelta
import logging

import meteireann

from homeassistant.const import (
    CONF_ELEVATION,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    LENGTH_FEET,
    LENGTH_METERS,
)
from homeassistant.core import Config, HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.util.distance import convert as convert_distance
import homeassistant.util.dt as dt_util

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

UPDATE_INTERVAL = timedelta(minutes=60)


async def async_setup(hass: HomeAssistant, config: Config) -> bool:
    """Set up configured Met Éireann."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass, config_entry):
    """Set up Met Éireann as config entry."""

    warning_data = MetEireannWarningData(
        hass, config_entry.data, hass.config.units.is_metric
    )
    warning_data.init_data()

    async def _async_update_data():
        """Fetch data from Met Éireann."""
        try:
            return await warning_data.fetch_data()
        except Exception as err:
            raise UpdateFailed(f"Update failed: {err}") from err

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_method=_async_update_data,
        update_interval=UPDATE_INTERVAL,
    )
    await coordinator.async_refresh()

    hass.data[DOMAIN][config_entry.entry_id] = coordinator

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "weather_warning")
    )

    return True


async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(config_entry, "weather_warning")
    hass.data[DOMAIN].pop(config_entry.entry_id)

    return True


class MetEireannWarningData:
    """Keep data for Met Éireann weather entities."""

    def __init__(self, hass, config, is_metric):
        """Initialise the weather entity data."""
        self.hass = hass
        self._config = config
        self._is_metric = is_metric
        self._warning_data = None
        self.current_warning_data = {}
        # self.daily_forecast = None
        # self.hourly_forecast = None

    def init_data(self):
        """Weather data inialization - get the coordinates."""
        latitude = self._config[CONF_LATITUDE]
        longitude = self._config[CONF_LONGITUDE]
        elevation = self._config[CONF_ELEVATION]

        if not self._is_metric:
            elevation = int(
                round(convert_distance(elevation, LENGTH_FEET, LENGTH_METERS))
            )

        self._warning_data = meteireann.WarningData(
            async_get_clientsession(self.hass),
            latitude=latitude,
            longitude=longitude,
            altitude=elevation,
        )

    async def fetch_data(self):
        """Fetch data from API - (current weather and forecast)."""
        await self._warning_data.fetching_data()
        self.current_warning_data = self._warning_data.get_warnings()
        # time_zone = dt_util.DEFAULT_TIME_ZONE
        # self.daily_forecast = self._warning_data.get_forecast(time_zone, False)
        # self.hourly_forecast = self._weather_data.get_forecast(time_zone, True)
        return self
