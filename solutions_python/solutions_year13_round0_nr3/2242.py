#!/usr/bin/python

from math import sqrt

def palindrome(i):
    i = str(i)
    first_half = i[:(len(i) / 2) + len(i) % 2]
    second_half = i[len(i) / 2:][::-1]
    if first_half == second_half:
        return True
    return False

def compute(board):
    res = 0
    ll = sqrt(board[0])
    limits = [int(ll) if round(ll, 0) == ll else int(ll) + 1, int(sqrt(board[1]))]
    for i in range(limits[0], limits[1] + 1):
        if palindrome(i) and palindrome(i ** 2):
            res += 1
    return res

def main():
    T = input()
    for t in range(T):
        board = map(int, raw_input().split())
        print "Case #%d: %s" % (t + 1, compute(board))

if __name__ == "__main__":
    main()
