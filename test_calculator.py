import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test1_add(self):
        self.assertEqual(self.calc.add(5, 8), 13)

    # Add the following test methods to the TestCalculator class:
    def test_sub(self):
        self.assertEqual(self.calc.subtract(20, 8), 12)

    def test1_sub(self):
        self.assertEqual(self.calc.subtract(30, 22), 8)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(12, 7), 84)

    def test1_mul(self):
        self.assertEqual(self.calc.multiply(25, 3), 75)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(12, 11), 1)

    def test1_div(self):
        self.assertEqual(self.calc.divide(32, 4), 8)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(7, 5), 2)

    def test1_mod(self):
        self.assertEqual(self.calc.modulo(44, 5), 4)

if __name__ == '__main__':
    unittest.main()