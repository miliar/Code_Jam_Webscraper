#!/usr/bin/env python3
import sys

def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs)
    pass

def isTidy(number):
    eprint("Testing number {}".format(number))
    for index in range(len(str(number)) - 1, 0, -1):
        if not all(int(digit) <= int(str(number)[index]) for digit in str(number)[:index]):
            return index
    return True

t = int(input())
for i in range(1, t + 1):
    number = int(input())
    while True:
        if number == 0:
            break
        digit = isTidy(number)
        if digit is True:
            break
        subtract = int(str(number)[digit:]) + 1
        eprint("Subtracting {}".format(subtract))
        number -= subtract

    print("Case #{}: {}".format(i, number))
