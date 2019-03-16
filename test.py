import unittest

from user import User
from unittest.mock import MagicMock


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        a = User()
        a.return_random = MagicMock(return_value=3)
        self.assertEqual(a.add_two_numbers(4, 3), 10)


if __name__ == '__main__':
    unittest.main()