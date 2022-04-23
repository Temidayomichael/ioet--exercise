import unittest
import ioet
import re


class TestStringMethods(unittest.TestCase):

    def test_regex(self):

        self.assertTrue(re.match("^[a-zA-Z]+=((MO|TU|WE|TH|FR|SA|SU)(([0-1]?[0-9]|2[0-3]):[0-5][0-9])-(([0-1]?[0-9]|2[0-3]):[0-5][0-9]),?)+$",
                        "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"))

    def test_calculateSalary(self):
        payPerHr = ioet.weekdaysPayPerHr

        # test for 10:00-12:00 within same time range
        self.assertEqual(ioet.calculateSalary(
            '10:00', '12:00', payPerHr), 30)
        # test for 10:50-14:00 within same time range with seconds
        self.assertEqual(ioet.calculateSalary(
            '10:00', '14:20', payPerHr), 65)
        
        # test for 08:00-22:00 outside extended time range
        self.assertEqual(ioet.calculateSalary(
            '08:00', '22:00', payPerHr), 240)

        # test for 08:00-22:50 outside extended time range with seconds
        self.assertEqual(ioet.calculateSalary(
            '08:00', '22:50', payPerHr), 257)

        



if __name__ == '__main__':
    unittest.main()
