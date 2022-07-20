"""
Unit tests for the calculator library
"""

import calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertTrue(4 == calculator.add(2, 2))

    def test_subtraction(self):
        self.assertTrue(2 == calculator.subtract(4, 2))

    def test_division(self):
        self.assertTrue(2 == calculator.divide(4, 2))


if __name__ == '__main__':
    unittest.main()
