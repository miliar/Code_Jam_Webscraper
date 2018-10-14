from math import sqrt,log,floor

def palindrome(x):
    digits = list()
    while x != 0:
        digits.append(x%10)
        x = x//10
    while len(digits) != 0:
        if digits[0] == digits[-1]:
            digits = digits[1:-1]
        else:
            return False
    return True

def fair_and_square(A,B):
    sqrt_A = sqrt(A)
    sqrt_B = sqrt(B)
    minimum = floor(sqrt_A)
    maximum = floor(sqrt_B)
    if minimum == sqrt_A:
        i = minimum
    else:
        i = minimum + 1
    fair_square = 0
    while i <= maximum:
        if palindrome(i) and palindrome(i**2):
            fair_square += 1
        i += 1
    return fair_square

if __name__ == '__main__':
    number = int(input())
    for i in range(number):
        a_b = input().split(' ')
        A = int(a_b[0])
        B = int(a_b[1])
        print("Case #" + str(i+1) + ": " + str(fair_and_square(A,B))) 
