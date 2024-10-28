# Inaccurate calculation demonstration
a = 1.0000001
b = 1.0000000
result = a - b

print("Expected result: 0.0000001")
print("Calculated result (limited by floating-point precision):", result)

##############################################################################################

# Round-off error example
n = 10**6
small_value = 0.0001
expected_sum = n * small_value

actual_sum = 0.0
for i in range(n):
    actual_sum += small_value

hardcoded_expected_sum = 100.0

print("Hardcoded expected sum:", hardcoded_expected_sum)
print("Actual computed sum (affected by round-off):", actual_sum)


########################################################################################

# Underflow and Overflow Example

# Underflow example
small_number1 = 10**-200
small_number2 = 10**-200
underflow_result = small_number1 * small_number2  # Expected to approach zero

print("Underflow result:", underflow_result)

# Overflow example
large_number1 = 10**200
large_number2 = 10**200

try:
    overflow_result = large_number1 * large_number2
    expected_overflow_result = float('inf')
except OverflowError as e:
    overflow_result = str(e)
    expected_overflow_result = str(e)

print("Overflow result:", overflow_result)
print("Hardcoded expected overflow result:", expected_overflow_result)


#############################################################################################

# Associative property violation example
a = 1.0
b = 1e-16
c = 1e-16

result1 = (a + b) + c
result2 = a + (b + c)

expected_result = 1.0

print("Result of (a + b) + c:", result1)
print("Result of a + (b + c):", result2)
print("Hardcoded expected result for both:", expected_result)
print("Difference due to associative property violation (first result):", result1 - expected_result)
print("Difference due to associative property violation (second result):", result2 - expected_result)
