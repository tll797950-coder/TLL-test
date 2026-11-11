"""Tests for :mod:`bubble_sort`."""

import random
import unittest

from bubble_sort import bubble_sort


class BubbleSortTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_item(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([0, -3, 7, -1, 2]), [-3, -1, 0, 2, 7])

    def test_floats(self):
        self.assertEqual(bubble_sort([2.5, 1.0, 3.25]), [1.0, 2.5, 3.25])

    def test_does_not_mutate_input(self):
        original = [4, 2, 9, 1]
        bubble_sort(original)
        self.assertEqual(original, [4, 2, 9, 1])

    def test_accepts_tuple_and_other_iterables(self):
        self.assertEqual(bubble_sort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(bubble_sort(range(5, 0, -1)), [1, 2, 3, 4, 5])

    def test_random_lists_match_builtin_sort(self):
        rng = random.Random(2026)
        for _ in range(50):
            values = [rng.randint(-100, 100) for _ in range(rng.randint(0, 30))]
            self.assertEqual(bubble_sort(values), sorted(values))


if __name__ == "__main__":
    unittest.main()
