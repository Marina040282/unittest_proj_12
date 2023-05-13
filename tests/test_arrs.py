import unittest
import utils.arrs as arrs


class TestArrs(unittest.TestCase):
    def test_get(self):

        arr = [1, 2, 3, 4]
        self.assertEqual(arrs.get(arr, 0), 1)
        self.assertEqual(arrs.get(arr, -1), 4)
        self.assertEqual(arrs.get(arr, 4), None)
        self.assertEqual(arrs.get(arr, 4, 'default'), 'default')
        self.assertEqual(arrs.get(arr, -5, 'default'), 'default')
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")


    def test_my_slice(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(arrs.my_slice(arr), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(arrs.my_slice(arr, 0, 5), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice(arr, -5), [6, 7, 8, 9, 10])
        self.assertEqual(arrs.my_slice(arr, 0, -5), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice(arr, 3, 7), [4, 5, 6, 7])
        self.assertEqual(arrs.my_slice(arr, 3, -3), [4, 5, 6, 7])
        self.assertEqual(arrs.my_slice([], 0, 1), [])
        self.assertEqual(arrs.my_slice([], -1, 0), [])