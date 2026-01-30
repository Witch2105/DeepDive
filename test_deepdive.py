# test_deepdive.py
"""
Tests for DeepDive module.
"""

import unittest
from deepdive import DeepDive

class TestDeepDive(unittest.TestCase):
    """Test cases for DeepDive class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeepDive()
        self.assertIsInstance(instance, DeepDive)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeepDive()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
