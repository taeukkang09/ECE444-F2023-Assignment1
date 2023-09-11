import unittest
from utils import Utils


class TestUtils(unittest.TestCase):
    def test_reversed_int(self):
        self.assertEqual(Utils.reversed(17563), 36571)

    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            Utils.reversed(1.7563)

    def test_reversed_string(self):
        with self.assertRaises(ValueError):
            Utils.reversed("17563")

    def test_formatter_int(self):
        self.assertEqual(Utils.formatter(255), ("0b11111111", "0o377"))

    def test_formatter_float(self):
        with self.assertRaises(ValueError):
            Utils.formatter(2.55)

    def test_formatter_string(self):
        with self.assertRaises(ValueError):
            Utils.formatter("255")


if __name__ == "__main__":
    unittest.main()
