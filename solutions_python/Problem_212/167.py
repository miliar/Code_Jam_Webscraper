#!/usr/bin/env python3

def read_ints():
    return list(map(int, input().split(' ')))

def solve2(n0, n1):
    return n0 + n1//2 + (1 if n1%2 > 0 else 0)

def solve3(n0, n1, n2):
    k = min(n1, n2)
    return n0 + k + (n1-k)//3 + (n2-k)//3 + (1 if (n1-k)%3 + (n2-k)%3 > 0 else 0)

def solve4(n0, n1, n2, n3):
    a1 = solve4impl(n0, n1, n2, n3)
    a2 = solve4impl(n0, n3, n2, n1)
    if a1 != a2:
        raise Exception("solve4 inconsistent on {}: {} != {}".format([n0, n1, n2, n3], a1, a2))
    return a1

def solve4impl(n0, n1, n2, n3):
    k2 = n2//2
    k13 = min(n1, n3)
    n1 -= k13
    n2 = n2%2
    n3 -= k13
    k2x = 0
    if n2 == 1:
        if n1 >= 2 and n1 % 4 != 0:
            k2x = 1
            n2 -= 1
            n1 -= 2
        elif n3 >= 2:
            k2x = 1
            n2 -= 1
            n3 -= 2
    return n0 + k13 + k2 + k2x + (n1//4) + (n3//4) + (1 if n2 + (n1%4) + (n3%4) > 0 else 0)

def main():
    ts = int(input())
    for ti in range(ts):
        n, p = read_ints()
        freq = [0] * p
        for i in read_ints():
            freq[i%p] += 1
        if p == 2:
            ans = solve2(*freq)
        elif p == 3:
            ans = solve3(*freq)
        elif p == 4:
            ans = solve4(*freq)
        else:
            raise Exception("Invalid P: {}".format(p))
        print("Case #{}: {}".format(ti+1, ans))

if __name__ == '__main__':
    main()
