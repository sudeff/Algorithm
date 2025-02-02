# Assingment 1 Karatsuba's Algoritm

def karatsuba_multiplication(x, y):
    # Base case for single-digit numbers
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y (10^32 baseinde ikiye bölüyoruz)
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # Recursive calls
    z0 = karatsuba_multiplication(low_x, low_y)
    z1 = karatsuba_multiplication((low_x + high_x), (low_y + high_y))
    z2 = karatsuba_multiplication(high_x, high_y)

    # Combine the results
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Given 64-digit numbers
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# Calculate the product using Karatsuba's algorithm
result = karatsuba_multiplication(num1, num2)
result
