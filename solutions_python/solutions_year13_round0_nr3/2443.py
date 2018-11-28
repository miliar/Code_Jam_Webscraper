from math import sqrt

def read_case():
    a, b = input().split()
    return int(a), int(b)

def palindrome(num):
    s = str(num)
    return s == s[::-1]

def solve_case(interval):
    cnt = 0
    a, b = interval
    for i in range(a, b+1):
        if palindrome(i):
            r = int(sqrt(i))
            if r*r == i and palindrome(r):
                cnt += 1
    return cnt

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        res = solve_case(read_case())
        print("Case #{}: {}".format(t, res))
