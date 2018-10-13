import time
fairly_squarables = [1,2,3,11,22,101,202,111,212,121,1001,2002,1111,10001,20002,11011,10101,20102,11111,10201,11211,100001,200002,110011,101101,111111,1000001,2000002,1100011,1010101,1110111,1001001,2001002,1101011,1011101,1111111,1002001,1102011,1012101]

def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def is_square_palindrome(n):
    sq = n * n
    return is_palindrome(sq)

def is_fair_and_square(n):
    return is_palindrome(n) and is_square_palindrome(n)

def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        low, high = map(int, input().split())
        l_sqrt, h_sqrt = map(isqrt, (low, high))
        num_fs = len([i for i in fairly_squarables if low <= i*i <= high])
        """if l_sqrt * l_sqrt < low: l_sqrt += 1
        if (h_sqrt + 1) ** 2 == h_sqrt: h_sqrt += 1
        for test in range(l_sqrt, h_sqrt + 1):
            if is_fair_and_square(test):
                num_fs += 1
                """
        print("Case #{}: {}".format(case, num_fs))

if __name__ == '__main__':
    main()
