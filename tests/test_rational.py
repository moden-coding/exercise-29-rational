#!/usr/bin/env python3

import unittest

from src.rational import Rational


class TestRational(unittest.TestCase):

    def test_print(self):
        r1 = Rational(1, 4)
        result = str(r1)
        self.assertNotRegex(
            result, r'<src\.rational\.Rational object at 0x[0-9a-f]+>',
            msg="The rational object is not printable: define '__str__' method!")
        self.assertIn(
            "1", result,
            msg="Printing Rational(1, 4) should show the numerator 1: define "
                "'__str__' method!")
        self.assertIn(
            "4", result,
            msg="Printing Rational(1, 4) should show the denominator 4: "
                "define '__str__' method!")

    def test_proddiv(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 3)
        self.assertEqual(
            r1 * r2, Rational(2, 12),
            msg="Incorrect result for operation %s * %s!" % (r1, r2))
        self.assertEqual(
            r1 / r2, Rational(3, 8),
            msg="Incorrect result for operation %s / %s!" % (r1, r2))

    def test_plusminus(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 3)
        self.assertEqual(
            r1 + r2, Rational(11, 12),
            msg="Incorrect result for operation %s + %s!" % (r1, r2))
        self.assertEqual(
            r1 - r2, Rational(-5, 12),
            msg="Incorrect result for operation %s - %s!" % (r1, r2))

    def test_comparison(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 3)
        self.assertEqual(
            r1 == r2, False,
            msg="Incorrect result for operation %s == %s!" % (r1, r2))
        self.assertEqual(
            r1 < r2, True,
            msg="Incorrect result for operation %s < %s!" % (r1, r2))
        self.assertEqual(
            r1 > r2, False,
            msg="Incorrect result for operation %s > %s!" % (r1, r2))

    def test_equal_fractions_with_different_terms(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 4)
        self.assertEqual(
            r1 == r2, True,
            msg="Rational(1, 2) and Rational(2, 4) represent the same value "
                "and must compare equal, even though the numerator and "
                "denominator differ.")

    def test_addition_with_whole_number_result(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        self.assertEqual(
            r1 + r2, Rational(1, 1),
            msg="Rational(1, 2) + Rational(1, 2) should be Rational(1, 1) "
                "(i.e. the whole number 1).")


if __name__ == '__main__':
    unittest.main()
