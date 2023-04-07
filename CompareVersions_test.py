import unittest
from CompareVersions import compare_versions


class TestClass(unittest.TestCase):

    def testCompareVersions1(self):
        self.assertEqual(-1, compare_versions('0.1', '1.1'))

    def testCompareVersions2(self):
        self.assertEqual(1, compare_versions('1.2', '1.1'))

    def testCompareVersions3(self):
        self.assertEqual(0, compare_versions('1.2', '1.2'))

    def testCompareVersions4(self):
        self.assertEqual(-1, compare_versions('1.2', '1.2.9.9.9.9'))

    def testCompareVersions5(self):
        self.assertEqual(1, compare_versions('1.3', '1.2.9.9.9.9'))

    def testCompareVersions6(self):
        self.assertEqual(0, compare_versions('1.3', '1.3'))

    def testCompareVersions7(self):
        self.assertEqual(-1, compare_versions('1.3', '1.3.4'))

    def testCompareVersions8(self):
        self.assertEqual(1, compare_versions('1.10', '1.3.4'))

    def testCompareVersions9(self):
        self.assertEqual(0, compare_versions('1.10', '1.10'))


if __name__ == '__main__':
    unittest.main()
