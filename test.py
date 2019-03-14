import unittest

from zadanie import *


class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-3, 3), 0)
        self.assertEqual(suma(2, 4), 6)

    def test_roznica(self):
        self.assertEqual(roznica(2, 3), -1)
        self.assertEqual(roznica(-3, 3), -6)
        self.assertEqual(roznica(2, 4), -2)


if __name__ == '__main__':
    unittest.main()
