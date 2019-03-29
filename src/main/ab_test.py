import numpy as np
import scipy.stats as stats


class ABTest:

  HYPOTHESIS_ONE_SIDED = 'one-sided'
  HYPOTHESIS_TWO_SIDED = 'two-sided'

  def __init__(
    self,
    visitor_control,
    conversion_control,
    visitor_variation,
    conversion_variation,
    hypothesis=HYPOTHESIS_TWO_SIDED,
    confidence=0.95
  ):

    ABTest.__validate_hypothesis(hypothesis)
    ABTest.__validate_confidence(confidence)

    self.__visitor_control = np.float_(visitor_control)
    self.__conversion_control = np.float_(conversion_control)
    self.__visitor_variation = np.float_(visitor_variation)
    self.__conversion_variation = np.float_(conversion_variation)
    self.__confidence = float(confidence)
    self.__hypothesis = hypothesis

  def set_visitor_control(self, visitor_control):
    self.__visitor_control = np.float_(visitor_control)

  def set_conversion_control(self, conversion_control):
    self.__conversion_control = np.float_(conversion_control)

  def set_visitor_variation(self, visitor_variation):
    self.__visitor_variation = np.float_(visitor_variation)

  def set_conversion_variation(self, conversion_variation):
    self.__conversion_variation = np.float_(conversion_variation)

  def set_hypothesis(self, hypothesis):
    ABTest.__validate_hypothesis(hypothesis)
    self.__hypothesis = hypothesis

  def set_confidence(self, confidence):
    ABTest.__validate_confidence(confidence)
    self.__confidence = float(confidence)

  def get_conversion_rate_control(self):
    return self.__conversion_control / self.__visitor_control

  def get_conversion_rate_variation(self):
    return self.__conversion_variation / self.__visitor_variation

  def get_standard_error_control(self):
    return ABTest.__calculate_standard_error(self.__visitor_control, self.get_conversion_rate_control())

  def get_standard_error_variation(self):
    return ABTest.__calculate_standard_error(self.__visitor_variation, self.get_conversion_rate_variation())

  def get_standard_error_difference(self):
    standard_error_control = self.get_standard_error_control()
    standard_error_variation = self.get_standard_error_variation()
    return np.sqrt(np.power(standard_error_control, 2) + np.power(standard_error_variation, 2))

  def get_z_score(self):
    return (self.get_conversion_rate_variation() - self.get_conversion_rate_control()) / self.get_standard_error_difference()

  def get_p_value(self):
    return stats.norm.sf(abs(self.get_z_score()))

  def get_relative_uplift_conversion_rate(self):
    return (self.get_conversion_rate_variation() - self.get_conversion_rate_control()) / self.get_conversion_rate_control()

  def is_significant(self):
    alpha = (1 - self.__confidence)
    if (self.__hypothesis == ABTest.HYPOTHESIS_TWO_SIDED):
      alpha /= 2
    return self.get_p_value() < alpha

  @staticmethod
  def __calculate_conversion_rate(visitor, conversion):
    return visitor / conversion

  @staticmethod
  def __calculate_standard_error(visitor, conversion_rate):
    return np.sqrt(conversion_rate * (1 - conversion_rate) / visitor)

  @staticmethod
  def __validate_hypothesis(hypothesis):
    if (hypothesis != ABTest.HYPOTHESIS_ONE_SIDED and hypothesis != ABTest.HYPOTHESIS_TWO_SIDED):
      raise Exception("Hypothesis is neither {} nor {}.".format(ABTest.HYPOTHESIS_ONE_SIDED, ABTest.HYPOTHESIS_TWO_SIDED))

  @staticmethod
  def __validate_confidence(confidence):
    if (confidence < 0 and confidence > 1):
      raise Exception("Confidence must be between 0 and 1.")