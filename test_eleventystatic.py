# test_eleventystatic.py
"""
Tests for EleventyStatic module.
"""

import unittest
from eleventystatic import EleventyStatic

class TestEleventyStatic(unittest.TestCase):
    """Test cases for EleventyStatic class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EleventyStatic()
        self.assertIsInstance(instance, EleventyStatic)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EleventyStatic()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
