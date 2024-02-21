import unittest

from util.pylib import util


class TestCleanText(unittest.TestCase):
    def test_clean_text_01(self):
        """It preserves line breaks."""
        self.assertEqual(util.clean_text("one\ntwo\nthree"), "one two three")

    def test_clean_text_02(self):
        """It removes soft hyphens."""
        self.assertEqual(util.clean_text("; leaf­ lets"), "; leaflets")

    def test_clean_text_03(self):
        """It removes soft hyphens on multiple lines."""
        self.assertEqual(util.clean_text("leaf­ lets\nleaf­ lets"), "leaflets leaflets")
