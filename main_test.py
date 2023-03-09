import unittest

from main import encrypt_caesar
from main import decrypt_caesar

class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(encrypt_caesar("successful unit test", 5), 'XZHHJXXKZQZSNYYJXY')


    def test_upper2(self):
        self.assertEqual(encrypt_caesar("finally done!", 13), 'SVANYYLQBAR')


    def test_upper3(self):
        self.assertEqual(decrypt_caesar("XZHHJXXKZQ ZSNY YJXY", 5), 'SUCCESSFULUNITTEST')


    def test_upper4(self):
        self.assertEqual(decrypt_caesar("SVANYYL QBAR", 13), 'FINALLYDONE')


if __name__ == '__main__':
    unittest.main()