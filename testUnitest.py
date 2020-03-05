import unittest
import geometry
import geometry2


class PlaneTestCase(unittest.TestCase):

    def test_point_input(self):
        m = geometry2.enter_the_point_2()
        self.assertEqual(type(m), list)

   # def test_find_third_point(self):
    #    m = geometry2.find_third_point()



if __name__ == "__name__":
    unittest.main()