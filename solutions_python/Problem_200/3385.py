#!/usr/bin/env python
# encoding utf-8

DEBUG = False

def debug(string):
    if DEBUG:
        print("DEBUG: {}".format(string))

def is_tidy(numbers):
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            return False
    return True

def tider(n):
    while not is_tidy(n):
        for i in range(0, len(n)-1):
            if n[i] > n[i+1]:
                debug("{} > {}".format(n[i], n[i+1]))
                n[i] -= 1
                for j in range(i+1, len(n)):
                    n[j] = 9
    debug("tider resultou em : {}".format(n))

q = input()
for case in range(1,q+1):
    count = 0
    line = str(raw_input())
    letters = list(line)
    numbers = map(int, line)
    debug("Linha lida: {}".format(numbers))
    debug(is_tidy(numbers))
    tider(numbers)
    final = ''
    for i in range(len(numbers)):
        if numbers[i] != 0:
            final += str(numbers[i])
    print("Case #{}: {}".format(case, final))
