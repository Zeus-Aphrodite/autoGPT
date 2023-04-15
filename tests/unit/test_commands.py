from autogpt import commands
import unittest
from unittest.mock import patch, MagicMock


class TestCommands(unittest.TestCase):
    def test_make_agent(self):
        with patch("openai.ChatCompletion.create") as mock:
            obj = MagicMock()
            obj.response.choices[0].messages[0].content = "Test message"
            mock.return_value = obj
            commands.start_agent("Test Agent", "chat", "Hello, how are you?", "gpt2")
            agents = commands.list_agents()
            self.assertEqual("List of agents:\n0: chat", agents)
            commands.start_agent("Test Agent 2", "write", "Hello, how are you?", "gpt2")
            agents = commands.list_agents()
            self.assertEqual("List of agents:\n0: chat\n1: write", agents)
