from unittest import mock
from homeassistant import data_entry_flow
from custom_components.ferroamp import config_flow, CONF_NAME, CONF_PREFIX
from pytest_homeassistant_custom_component.common import MockConfigEntry
from custom_components.ferroamp.const import (
    CONF_INTERVAL,
    CONF_PRECISION_BATTERY,
    CONF_PRECISION_CURRENT,
    CONF_PRECISION_ENERGY,
    CONF_PRECISION_FREQUENCY,
    CONF_PRECISION_TEMPERATURE,
    CONF_PRECISION_VOLTAGE
)


async def test_flow_user_init(hass, mqtt_mock):
    """Test the initialization of the form in the first step of the config flow."""
    result = await hass.config_entries.flow.async_init(
        config_flow.DOMAIN, context={"source": "user"}
    )
    expected = {
        "data_schema": config_flow.TOPIC_SCHEMA,
        "description_placeholders": None,
        "errors": {},
        "flow_id": mock.ANY,
        "handler": "ferroamp",
        "step_id": "user",
        "type": "form",
        "last_step": None,
    }
    assert expected == result


async def test_flow_user_step_no_input(hass, mqtt_mock):
    """Test appropriate error when no input is provided."""
    _result = await hass.config_entries.flow.async_init(
        config_flow.DOMAIN, context={"source": "user"}
    )
    result = await hass.config_entries.flow.async_configure(
        _result["flow_id"], user_input={CONF_NAME: "", CONF_PREFIX: ""}
    )
    assert {"base": "name"} == result["errors"]


async def test_flow_user_creates_config_entry(hass, mqtt_mock):
    """Test the config entry is successfully created."""
    _result = await hass.config_entries.flow.async_init(
        config_flow.DOMAIN, context={"source": "user"}
    )
    result = await hass.config_entries.flow.async_configure(
        _result["flow_id"], user_input={}
    )
    expected = {
        "version": 1,
        "type": "create_entry",
        "flow_id": mock.ANY,
        "handler": "ferroamp",
        "options": {},
        "title": "Ferroamp",
        "data": {
            "name": "Ferroamp",
            "prefix": "extapi",
        },
        "description": None,
        "description_placeholders": None,
        "result": mock.ANY,
    }

    assert expected == {k: v for k,v in result.items() if k != "context"}
    await hass.async_block_till_done()


async def test_options_flow(hass, mqtt_mock):
    """Test config flow options."""
    config_entry = MockConfigEntry(
        domain=config_flow.DOMAIN,
        unique_id="ferroamp",
        data={
            CONF_NAME: "Ferroamp",
            CONF_PREFIX: "extapi",
        },
    )
    config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    # show initial form
    result = await hass.config_entries.options.async_init(config_entry.entry_id)
    assert "form" == result["type"]
    assert "init" == result["step_id"]
    assert {} == result["errors"]

    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        user_input={
            CONF_INTERVAL: 20,
            CONF_PRECISION_BATTERY: 1,
            CONF_PRECISION_CURRENT: 2,
            CONF_PRECISION_ENERGY: 3,
            CONF_PRECISION_FREQUENCY: 6,
            CONF_PRECISION_TEMPERATURE: 4,
            CONF_PRECISION_VOLTAGE: 5
        }
    )
    assert result["type"] == data_entry_flow.RESULT_TYPE_CREATE_ENTRY
    assert result["data"] == {
        CONF_INTERVAL: 20,
        CONF_PRECISION_BATTERY: 1,
        CONF_PRECISION_CURRENT: 2,
        CONF_PRECISION_ENERGY: 3,
        CONF_PRECISION_FREQUENCY: 6,
        CONF_PRECISION_TEMPERATURE: 4,
        CONF_PRECISION_VOLTAGE: 5
    }
    assert config_entry.data == {
        CONF_NAME: "Ferroamp",
        CONF_PREFIX: "extapi"
    }
    assert config_entry.options == {
        CONF_INTERVAL: 20,
        CONF_PRECISION_BATTERY: 1,
        CONF_PRECISION_CURRENT: 2,
        CONF_PRECISION_ENERGY: 3,
        CONF_PRECISION_FREQUENCY: 6,
        CONF_PRECISION_TEMPERATURE: 4,
        CONF_PRECISION_VOLTAGE: 5
    }
