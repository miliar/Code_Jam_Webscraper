#!/usr/bin/env python

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_fair_and_squares(n):
    return [i**2 for i in xrange(int(n ** 0.5 + 0.000001)) if (
            is_palindrome(i) and is_palindrome(i**2))]

if __name__ == "__main__":
    fair_and_squares = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]
    for i in xrange(int(raw_input())):
        l, r = [int(s) for s in raw_input().split()]
        ans = sum(l <= v <= r for v in fair_and_squares)
        print "Case #%d: %d" % (i + 1, ans)
