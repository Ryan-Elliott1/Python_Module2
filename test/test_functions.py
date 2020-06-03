import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(camper_age_input.convert_to_months(3), 36)


if __name__ == '__main__':
    unittest.main()

