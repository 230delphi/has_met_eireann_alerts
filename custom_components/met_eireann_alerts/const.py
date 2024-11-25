"""Constants for Met Éireann component."""
import logging

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    DOMAIN as WEATHER_DOMAIN,
)

ATTRIBUTION = "Data provided by Met Éireann"

DEFAULT_NAME = "Met Éireann Alerts"

DOMAIN = "met_eireann_alerts"

HOME_LOCATION_NAME = "Home"

ENTITY_ID_SENSOR_FORMAT_HOME = f"{WEATHER_DOMAIN}.met_eireann_{HOME_LOCATION_NAME}"

_LOGGER = logging.getLogger(".")

CONDITION_MAP = {
    ATTR_CONDITION_CLEAR_NIGHT: ["Dark_Sun"],
    ATTR_CONDITION_CLOUDY: ["Cloud"],
    ATTR_CONDITION_FOG: ["Fog"],
    ATTR_CONDITION_LIGHTNING_RAINY: [
        "LightRainThunderSun",
        "LightRainThunderSun",
        "RainThunder",
        "SnowThunder",
        "SleetSunThunder",
        "Dark_SleetSunThunder",
        "SnowSunThunder",
        "Dark_SnowSunThunder",
        "LightRainThunder",
        "SleetThunder",
        "DrizzleThunderSun",
        "Dark_DrizzleThunderSun",
        "RainThunderSun",
        "Dark_RainThunderSun",
        "LightSleetThunderSun",
        "Dark_LightSleetThunderSun",
        "HeavySleetThunderSun",
        "Dark_HeavySleetThunderSun",
        "LightSnowThunderSun",
        "Dark_LightSnowThunderSun",
        "HeavySnowThunderSun",
        "Dark_HeavySnowThunderSun",
        "DrizzleThunder",
        "LightSleetThunder",
        "HeavySleetThunder",
        "LightSnowThunder",
        "HeavySnowThunder",
    ],
    ATTR_CONDITION_PARTLYCLOUDY: [
        "LightCloud",
        "Dark_LightCloud",
        "PartlyCloud",
        "Dark_PartlyCloud",
    ],
    ATTR_CONDITION_RAINY: [
        "LightRainSun",
        "Dark_LightRainSun",
        "LightRain",
        "Rain",
        "DrizzleSun",
        "Dark_DrizzleSun",
        "RainSun",
        "Dark_RainSun",
        "Drizzle",
    ],
    ATTR_CONDITION_SNOWY: [
        "SnowSun",
        "Dark_SnowSun",
        "Snow",
        "LightSnowSun",
        "Dark_LightSnowSun",
        "HeavySnowSun",
        "Dark_HeavySnowSun",
        "LightSnow",
        "HeavySnow",
    ],
    ATTR_CONDITION_SNOWY_RAINY: [
        "SleetSun",
        "Dark_SleetSun",
        "Sleet",
        "LightSleetSun",
        "Dark_LightSleetSun",
        "HeavySleetSun",
        "Dark_HeavySleetSun",
        "LightSleet",
        "HeavySleet",
    ],
    ATTR_CONDITION_SUNNY: "Sun",
}
