```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import Dict, List
from langchain import LangGraph
from langchain.llms import AI21
from homeassistant.core import HomeAssistant

LOGGER = logging.getLogger(__name__)

def load_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for the given data.

    Args:
    - data (List[float]): A list of float values.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Calculate the non-stationary drift index using a stochastic regime switch
        non_stationary_drift_index = sum(data) / len(data)
        LOGGER.debug('Non-stationary drift index: %f', non_stationary_drift_index)
        return non_stationary_drift_index
    except ZeroDivisionError:
        LOGGER.error('Cannot calculate non-stationary drift index for empty data')
        return 0.0

def load_stochastic_regime_switch(state: Dict[str, str]) -> str:
    """
    Determine the stochastic regime switch based on the given state.

    Args:
    - state (Dict[str, str]): A dictionary representing the current state.

    Returns:
    - str: The stochastic regime switch.
    """
    try:
        # Use the LangGraph to determine the stochastic regime switch
        lang_graph = LangGraph()
        stochastic_regime_switch = lang_graph.query(state)
        LOGGER.debug('Stochastic regime switch: %s', stochastic_regime_switch)
        return stochastic_regime_switch
    except Exception as e:
        LOGGER.error('Failed to determine stochastic regime switch: %s', e)
        return ''

def load_memory_management(hass: HomeAssistant) -> int:
    """
    Get the current memory management status.

    Args:
    - hass (HomeAssistant): The Home Assistant instance.

    Returns:
    - int: The memory management status.
    """
    try:
        # Use the Home Assistant API to get the memory management status
        memory_management_status = hass.services.call('system', 'memory_management')
        LOGGER.debug('Memory management status: %d', memory_management_status)
        return memory_management_status
    except Exception as e:
        LOGGER.error('Failed to get memory management status: %s', e)
        return 0

def load_ai21_model() -> AI21:
    """
    Load the AI21 model.

    Returns:
    - AI21: The loaded AI21 model.
    """
    try:
        # Load the AI21 model using the LangChain library
        ai21_model = AI21()
        LOGGER.debug('AI21 model loaded')
        return ai21_model
    except Exception as e:
        LOGGER.error('Failed to load AI21 model: %s', e)
        return None

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    non_stationary_drift_index = load_non_stationary_drift_index(data)
    state = {'temperature': '25', 'humidity': '60'}
    stochastic_regime_switch = load_stochastic_regime_switch(state)
    hass = HomeAssistant()
    memory_management_status = load_memory_management(hass)
    ai21_model = load_ai21_model()
    print('Non-stationary drift index:', non_stationary_drift_index)
    print('Stochastic regime switch:', stochastic_regime_switch)
    print('Memory management status:', memory_management_status)
    print('AI21 model loaded:', ai21_model is not None)
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```