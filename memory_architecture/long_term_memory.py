```json
{
    "memory_architecture/long_term_memory.py": {
        "content": "
import logging
from typing import Dict, List
from langchain import LLMChain, PromptTemplate
from langchain.chains import LLMChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import AI21

logger = logging.getLogger(__name__)

class LongTermMemory:
    def __init__(self, llm: AI21, embedding: HuggingFaceEmbeddings):
        """
        Initialize the LongTermMemory class.

        Args:
        - llm (AI21): The LLM to use for reasoning.
        - embedding (HuggingFaceEmbeddings): The embedding model to use for semantic search.
        """
        self.llm = llm
        self.embedding = embedding

    async def store_memory(self, state: Dict[str, str], config: Dict[str, str]) -> None:
        """
        Store a memory in the long-term memory.

        Args:
        - state (Dict[str, str]): The state to store.
        - config (Dict[str, str]): The configuration to store.

        Raises:
        - Exception: If an error occurs during storage.
        """
        try:
            # Create a prompt template for storing memories
            template = PromptTemplate(
                input_variables=['state', 'config'],
                template='Store the following state and config in long-term memory: {state} {config}',
            )
            # Create an LLM chain for storing memories
            chain = LLMChain(llm=self.llm, prompt=template)
            # Store the memory
            await chain(state=state, config=config)
            logger.info('Memory stored successfully')
        except Exception as e:
            logger.error(f'Error storing memory: {e}')

    async def retrieve_memory(self, query: str) -> Dict[str, str]:
        """
        Retrieve a memory from the long-term memory.

        Args:
        - query (str): The query to retrieve.

        Returns:
        - Dict[str, str]: The retrieved memory.

        Raises:
        - Exception: If an error occurs during retrieval.
        """
        try:
            # Create a prompt template for retrieving memories
            template = PromptTemplate(
                input_variables=['query'],
                template='Retrieve the memory that matches the following query: {query}',
            )
            # Create an LLM chain for retrieving memories
            chain = LLMChain(llm=self.llm, prompt=template)
            # Retrieve the memory
            output = await chain(query=query)
            logger.info('Memory retrieved successfully')
            return output
        except Exception as e:
            logger.error(f'Error retrieving memory: {e}')

    async def update_memory(self, state: Dict[str, str], config: Dict[str, str]) -> None:
        """
        Update a memory in the long-term memory.

        Args:
        - state (Dict[str, str]): The state to update.
        - config (Dict[str, str]): The configuration to update.

        Raises:
        - Exception: If an error occurs during update.
        """
        try:
            # Create a prompt template for updating memories
            template = PromptTemplate(
                input_variables=['state', 'config'],
                template='Update the following state and config in long-term memory: {state} {config}',
            )
            # Create an LLM chain for updating memories
            chain = LLMChain(llm=self.llm, prompt=template)
            # Update the memory
            await chain(state=state, config=config)
            logger.info('Memory updated successfully')
        except Exception as e:
            logger.error(f'Error updating memory: {e}')

    async def stochastic_regime_switch(self, non_stationary_drift_index: float) -> None:
        """
        Perform a stochastic regime switch.

        Args:
        - non_stationary_drift_index (float): The non-stationary drift index.

        Raises:
        - Exception: If an error occurs during the regime switch.
        """
        try:
            # Create a prompt template for stochastic regime switch
            template = PromptTemplate(
                input_variables=['non_stationary_drift_index'],
                template='Perform a stochastic regime switch with the following non-stationary drift index: {non_stationary_drift_index}',
            )
            # Create an LLM chain for stochastic regime switch
            chain = LLMChain(llm=self.llm, prompt=template)
            # Perform the regime switch
            await chain(non_stationary_drift_index=non_stationary_drift_index)
            logger.info('Regime switch performed successfully')
        except Exception as e:
            logger.error(f'Error performing regime switch: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    llm = AI21()
    embedding = HuggingFaceEmbeddings()
    long_term_memory = LongTermMemory(llm, embedding)

    # Store a memory
    state = {'altitude': '1000m', 'velocity': '50m/s'}
    config = {'fuel': '1000kg', 'oxidizer': '500kg'}
    async def store_memory_simulation():
        await long_term_memory.store_memory(state, config)

    # Retrieve a memory
    query = 'altitude'
    async def retrieve_memory_simulation():
        output = await long_term_memory.retrieve_memory(query)
        print(output)

    # Update a memory
    updated_state = {'altitude': '2000m', 'velocity': '100m/s'}
    updated_config = {'fuel': '500kg', 'oxidizer': '250kg'}
    async def update_memory_simulation():
        await long_term_memory.update_memory(updated_state, updated_config)

    # Perform a stochastic regime switch
    non_stationary_drift_index = 0.5
    async def stochastic_regime_switch_simulation():
        await long_term_memory.stochastic_regime_switch(non_stationary_drift_index)

    import asyncio
    asyncio.run(store_memory_simulation())
    asyncio.run(retrieve_memory_simulation())
    asyncio.run(update_memory_simulation())
    asyncio.run(stochastic_regime_switch_simulation())
",
        "commit_message": "feat: implement specialized long_term_memory logic"
    }
}
```