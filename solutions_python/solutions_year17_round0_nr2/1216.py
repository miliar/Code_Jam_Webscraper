#! /usr/bin/env python3

def is_tidy(number):
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            return False
    return True

def decr(number, i):
    number[i]  -= 1
    while number[i] == -1:
        number[i] = 9
        i -= 1
        number[i] -= 1

def tidy(number):
    number = [int(c) for c in number]
    i = len(number)-1
    while not is_tidy(number):
        number[i] = 9
        decr(number, i-1)
        i -= 1
    return str(int(''.join(str(c) for c in number)))


if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        number = input()
        solution = tidy(number)
        print('Case #%d: %s' % (case+1, solution))
