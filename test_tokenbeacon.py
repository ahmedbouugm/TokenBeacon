# test_tokenbeacon.py
"""
Tests for TokenBeacon module.
"""

import unittest
from tokenbeacon import TokenBeacon

class TestTokenBeacon(unittest.TestCase):
    """Test cases for TokenBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenBeacon()
        self.assertIsInstance(instance, TokenBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
