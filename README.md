### AB Tester

AB Tester module provides a capability to test whether the AB Test is statistically significant or not.

#### Usage Example

```
ab_test = ABTest (
  80000,                        # visitor_control
  1600,                         # conversion_control
  80000,                        # visitor_variation
  1696,                         # conversion_variation
  ABTest.HYPOTHESIS_ONE_SIDED,  # hypothesis
  0.95                          # confidence
)
```

##### Conversion Rate of Control Variable
```
ab_test.get_conversion_rate_control() 

# Output: 0.02
```

##### Conversion Rate of Variation Variable
```
ab_test.get_conversion_rate_variation() 

# Output: 0.0212
```

##### Standard Error of Control Variable
```
ab_test.get_standard_error_control() 

# Output: 0.0004949747468305833
```

##### Standard Error of Variation Variable
```
ab_test.get_standard_error_variation() 

# Output: 0.0005092955919699286
```

##### Standard Error of Difference between Control Variable and Variation Variable
```
ab_test.get_standard_error_difference() 

# Output: 0.0007101985637833971
```

##### Z Score
```
ab_test.get_z_score() 

# Output: 1.689668300098093
```

##### P Value
```
ab_test.get_p_value() 

# Output: 0.045545715565839716
```

##### Relative Uplift of Conversion Rate
```
ab_test.get_relative_uplift_conversion_rate() 

# Output: 0.059999999999999984
```
