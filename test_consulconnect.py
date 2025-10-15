# test_consulconnect.py
"""
Tests for ConsulConnect module.
"""

import unittest
from consulconnect import ConsulConnect

class TestConsulConnect(unittest.TestCase):
    """Test cases for ConsulConnect class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ConsulConnect()
        self.assertIsInstance(instance, ConsulConnect)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ConsulConnect()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
