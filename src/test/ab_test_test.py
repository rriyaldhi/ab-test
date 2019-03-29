import unittest
import numpy as np
from ab_test import ABTest

class ABTestTest(unittest.TestCase):
  
  def test_one_sided_significant(self):
    ab_test = ABTest(
      80000,
      1600,
      80000,
      1696,
      ABTest.HYPOTHESIS_ONE_SIDED,
      0.95
    )
    self.assertEqual(ab_test.get_conversion_rate_control(), np.float_(0.02))
    self.assertEqual(ab_test.get_conversion_rate_variation(), np.float_(0.0212))
    self.assertEqual(ab_test.get_standard_error_control(), np.float_(0.0004949747468305833))
    self.assertEqual(ab_test.get_standard_error_variation(), np.float_(0.0005092955919699286))
    self.assertEqual(ab_test.get_standard_error_difference(), np.float_(0.0007101985637833971))
    self.assertEqual(ab_test.get_z_score(), np.float_(1.689668300098093))
    self.assertEqual(ab_test.get_p_value(), np.float_(0.045545715565839716))
    self.assertEqual(ab_test.get_relative_uplift_conversion_rate(), np.float_(0.059999999999999984))
    self.assertTrue(ab_test.is_significant())

  def test_one_sided_not_significant(self):
    ab_test = ABTest(
      80000,
      1600,
      80000,
      1690,
      ABTest.HYPOTHESIS_ONE_SIDED,
      0.95
    )
    self.assertEqual(ab_test.get_conversion_rate_control(), np.float_(0.02))
    self.assertEqual(ab_test.get_conversion_rate_variation(), np.float_(0.021125))
    self.assertEqual(ab_test.get_standard_error_control(), np.float_(0.0004949747468305833))
    self.assertEqual(ab_test.get_standard_error_variation(), np.float_(0.0005084133944808103))
    self.assertEqual(ab_test.get_standard_error_difference(), np.float_(0.000709566191195367))
    self.assertEqual(ab_test.get_z_score(), np.float_(1.5854757652767753))
    self.assertEqual(ab_test.get_p_value(), np.float_(0.056429139453271784))
    self.assertEqual(ab_test.get_relative_uplift_conversion_rate(), np.float_(0.05625000000000005))
    self.assertFalse(ab_test.is_significant())

  def test_two_sided_significant(self):
    ab_test = ABTest(
      80000,
      1600,
      80000,
      1700,
      ABTest.HYPOTHESIS_TWO_SIDED,
      0.90
    )
    self.assertEqual(ab_test.get_conversion_rate_control(), np.float_(0.02))
    self.assertEqual(ab_test.get_conversion_rate_variation(), np.float_(0.02125))
    self.assertEqual(ab_test.get_standard_error_control(), np.float_(0.0004949747468305833))
    self.assertEqual(ab_test.get_standard_error_variation(), np.float_(0.0005098827990332681))
    self.assertEqual(ab_test.get_standard_error_difference(), np.float_(0.0007106197779051749))
    self.assertEqual(ab_test.get_z_score(), np.float_(1.75902787800933))
    self.assertEqual(ab_test.get_p_value(), np.float_(0.03928638678142826))
    self.assertEqual(ab_test.get_relative_uplift_conversion_rate(), np.float_(0.06250000000000006))
    self.assertTrue(ab_test.is_significant())

  def test_two_sided_not_significant(self):
    ab_test = ABTest(
      80000,
      1600,
      80000,
      1700,
      ABTest.HYPOTHESIS_TWO_SIDED,
      0.99
    )
    self.assertEqual(ab_test.get_conversion_rate_control(), np.float_(0.02))
    self.assertEqual(ab_test.get_conversion_rate_variation(), np.float_(0.02125))
    self.assertEqual(ab_test.get_standard_error_control(), np.float_(0.0004949747468305833))
    self.assertEqual(ab_test.get_standard_error_variation(), np.float_(0.0005098827990332681))
    self.assertEqual(ab_test.get_standard_error_difference(), np.float_(0.0007106197779051749))
    self.assertEqual(ab_test.get_z_score(), np.float_(1.75902787800933))
    self.assertEqual(ab_test.get_p_value(), np.float_(0.03928638678142826))
    self.assertEqual(ab_test.get_relative_uplift_conversion_rate(), np.float_(0.06250000000000006))
    self.assertFalse(ab_test.is_significant())

if __name__ == '__main__':
  unittest.main()