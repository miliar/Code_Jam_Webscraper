#!/usr/bin/python

def solve():
    line = raw_input()
    pancake = list(line.split()[0])
    length = int(line.split()[1])

    flip = 0

    for i in range(len(pancake) - length + 1):
        if pancake[i] == '-':
            flip += 1
            for j in range(i, i + length):
                pancake[j] = '+' if pancake[j] == '-' else '-'

    if '-' in pancake:
        return 'IMPOSSIBLE'
    else:
        return flip


def main():
    ncase = int(raw_input())
    for i in range(0, ncase):
        print('Case #{}: {}'.format(i+1, solve()))

main()
