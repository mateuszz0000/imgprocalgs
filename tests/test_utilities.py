from unittest import TestCase
from imgprocalgs.algorithms import utilities


class TestRGBToHSV(TestCase):
    TEST_IMAGE = "tests/data/desert.jpg"

    def test_rgb_to_hsv(self):
        hsv = utilities.rgb_to_hsv(255, 255, 255)
        self.assertEqual(0, hsv.h)
        self.assertEqual(0, hsv.s)
        self.assertEqual(1.0, hsv.v)

        hsv = utilities.rgb_to_hsv(204, 221, 221)
        self.assertEqual(180, hsv.h)
        self.assertEqual(0.0769230769230769, hsv.s)
        self.assertEqual(0.8666666666666667, hsv.v)

        hsv = utilities.rgb_to_hsv(171, 205, 234)
        self.assertEqual(207.6190476190476, hsv.h)
        self.assertEqual(0.2692307692307693, hsv.s)
        self.assertEqual(0.9176470588235294, hsv.v)

        hsv = utilities.rgb_to_hsv(230, 10, 20)
        self.assertEqual(357.27272727272725, hsv.h)
        self.assertEqual(0.9565217391304348, hsv.s)
        self.assertEqual(0.9019607843137255, hsv.v)
