def is_power_of_8(n):
    if n <= 0:
        return False  # Powers of 8 must be positive
    
    while n % 8 == 0:
        n //= 8  # Keep dividing by 8

    return n == 1  # If n is reduced to 1, it was a power of 8

# Example usage
number = 64  # 8^2
if is_power_of_8(number):
    print(f"{number} is a power of 8.")
else:
    print(f"{number} is not a power of 8.")
