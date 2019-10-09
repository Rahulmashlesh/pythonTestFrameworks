

## UNITTEST REQ:
# You put your tests into classes as methods
# use special assertion methods in the unittest.TestCase class instead of built-in assert statement

import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()

# MOre about unittest:     https://docs.python.org/3/library/unittest.html
