import unittest
from src.main.lab import *


class TestCastingFunctions(unittest.TestCase):
    def test_int_to_float(self):
        result = int_to_float(5)
        self.assertEqual(type(result), float)
        self.assertEqual(result, 5.0)

    def test_float_to_int(self):
        result = float_to_int(3.14)
        self.assertEqual(type(result), int)
        self.assertEqual(result, 3)

    def test_str_to_int(self):
        result = str_to_int("10")
        self.assertEqual(type(result), int)
        self.assertEqual(result, 10)

    def test_str_to_float(self):
        result = str_to_float("3.14")
        self.assertEqual(type(result), float)
        self.assertEqual(result, 3.14)

    def test_int_to_str(self):
        result = int_to_str(10)
        self.assertEqual(type(result), str)
        self.assertEqual(result, "10")

    def test_float_to_str(self):
        result = float_to_str(3.14)
        self.assertEqual(type(result), str)
        self.assertEqual(result, "3.14")


if __name__ == '__main__':
    unittest.main()
