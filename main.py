def is_power_of_8(n):
    """Check if a number is a power of 8."""
    if n < 1:
        return False  # Powers of 8 are positive integers

    # Keep dividing n by 8 while it's divisible by 8
    while n % 8 == 0:
        n = n // 8

    # If the final result is 1, it's a power of 8
    return n == 1

# Test the function
test_numbers = [1, 8, 16, 64, 512, 1024, 4096]

for num in test_numbers:
    result = is_power_of_8(num)
    print(f"{num} is a power of 8: {result}")
