#!/usr/bin/python

from sys import stdin
import math

def fair_word(word):
    word = str(word)
    for i in range(len(word) / 2):
        if word[i] != word[-1 - i]:
            return False
    return True

def calc(A, B):
    root = int(math.ceil(math.sqrt(A)))
    num  = root**2
    result = 0
    while num <= B:
        if fair_word(num) and fair_word(root):
            result += 1
        root += 1
        num = root**2
    return result

if __name__ == '__main__':
    T = int(stdin.readline())
    for i in range(T):
        A, B = map(int, stdin.readline().split())
        print "Case #%d: %s" % (i + 1, calc(A, B))
