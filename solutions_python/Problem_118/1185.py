from math import sqrt, ceil, floor

def to_digits(a):
    digits = []
    while a:
        digits.append(a % 10)
        a /= 10
    return digits

def is_pal(a):
    digits = to_digits(a)
    return digits == digits[::-1]

def solve(a, b):
    res = 0
    for i in range(int(ceil(sqrt(a))), int(floor(sqrt(b))) + 1):
        if is_pal(i) and is_pal(i ** 2):
            # print i, i ** 2
            res += 1
    return res

def main():
    n = int(raw_input())
    for i in range(1, n + 1):
        a, b = map(int, raw_input().split())
        ans = solve(a, b)
        print "Case #%d: %d" % (i, ans)

if __name__ == '__main__':
    main()
