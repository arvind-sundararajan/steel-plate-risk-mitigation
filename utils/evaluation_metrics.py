```json
{
    "utils/evaluation_metrics.py": {
        "content": "
import logging
from typing import Dict, List
from langchain import StateGraph
from homeassistant.core import State

logger = logging.getLogger(__name__)

def calculate_non_stationary_drift_index(state: State, config: Dict) -> float:
    """
    Calculate the non-stationary drift index for the given state and configuration.

    Args:
    - state (State): The current state of the system.
    - config (Dict): The configuration dictionary.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Call the StateGraph method from LangGraph
        state_graph = StateGraph(state)
        non_stationary_drift_index = state_graph.calculate_drift_index()
        logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
        return non_stationary_drift_index
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        return None

def stochastic_regime_switch(state: State, config: Dict) -> bool:
    """
    Determine if a stochastic regime switch has occurred.

    Args:
    - state (State): The current state of the system.
    - config (Dict): The configuration dictionary.

    Returns:
    - bool: True if a stochastic regime switch has occurred, False otherwise.
    """
    try:
        # Call the StateGraph method from LangGraph
        state_graph = StateGraph(state)
        regime_switch = state_graph.check_regime_switch()
        logger.info(f'Stochastic regime switch: {regime_switch}')
        return regime_switch
    except Exception as e:
        logger.error(f'Error checking stochastic regime switch: {e}')
        return False

def evaluate_metrics(state: State, config: Dict) -> Dict:
    """
    Evaluate the metrics for the given state and configuration.

    Args:
    - state (State): The current state of the system.
    - config (Dict): The configuration dictionary.

    Returns:
    - Dict: A dictionary containing the evaluated metrics.
    """
    try:
        metrics = {}
        metrics['non_stationary_drift_index'] = calculate_non_stationary_drift_index(state, config)
        metrics['stochastic_regime_switch'] = stochastic_regime_switch(state, config)
        logger.info(f'Metrics: {metrics}')
        return metrics
    except Exception as e:
        logger.error(f'Error evaluating metrics: {e}')
        return {}

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    state = State('rocket', 'science')
    config = {'drift_index_threshold': 0.5}
    metrics = evaluate_metrics(state, config)
    print(metrics)
",
        "commit_message": "feat: implement specialized evaluation_metrics logic"
    }
}
```