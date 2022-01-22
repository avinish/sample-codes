import unittest
import base_conversion as b

class MyTestCase(unittest.TestCase):
    decNo = 20
    binaryNo = 10100
    octNo = 24
    hexNo = 14
    sepNo = 26

    def test_decimal_binary(self):
        self.assertEqual(b.base_conversion(self.decNo,10,2),self.binaryNo)

    def test_decimal_octal(self):
        self.assertEqual(b.base_conversion(self.decNo,10,8),self.octNo)

    def test_decimal_hex(self):
        self.assertEqual(b.base_conversion(self.decNo,10,16),self.hexNo)

    def test_decimal_sep(self):
        self.assertEqual(b.base_conversion(self.decNo,10,7),self.sepNo)

    def test_binary_decimal(self):
        self.assertEqual(b.base_conversion(self.binaryNo,2,10),self.decNo)

    def test_binary_octal(self):
        self.assertEqual(b.base_conversion(self.binaryNo,2,8),self.octNo)

    def test_binary_hex(self):
        self.assertEqual(b.base_conversion(self.binaryNo,2,16),self.hexNo)

    def test_octal_bin(self):
        self.assertEqual(b.base_conversion(self.octNo,8,2),self.binaryNo)

    def test_octal_decimal(self):
        self.assertEqual(b.base_conversion(self.octNo,8,10),self.decNo)

    def test_octal_hex(self):
        self.assertEqual(b.base_conversion(self.octNo,8,16),self.hexNo)

    def test_hex_bin(self):
        self.assertEqual(b.base_conversion(self.hexNo,16,2),self.binaryNo)

    def test_hex_octal(self):
        self.assertEqual(b.base_conversion(self.hexNo,16,8),self.octNo)

    def test_hex_decimal(self):
        self.assertEqual(b.base_conversion(self.hexNo,16,10),self.decNo)

    def test_hex_sep(self):
        self.assertEqual(b.base_conversion(self.hexNo, 16, 7), self.sepNo)




if __name__ == '__main__':
    unittest.main()
