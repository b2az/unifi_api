from homeassistant import core
import voluptuous as vol

from homeassistant.helpers import config_validation as cv

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Unifi API component."""
    hass.states.set("hello_world.Hello_World", "Works!")
    # @TODO: Add setup code.
    return True
