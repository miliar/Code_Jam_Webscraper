__author__ = 'antonkov'
import itertools

input = open('input', 'r')

def read_int():
    return int(input.readline())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_floats():
    return [float(x) for x in input.readline().split()]

t = read_int()
for test in range(t):
    print("Case #" + str(test + 1) + ": ", end="")
    n = read_int()
    a, b = sorted(read_floats()), sorted(read_floats())
    war = 0
    res_usual = 0
    for i in range(n):
        if a[i] > b[war]:
            war += 1
    for x in a:
        won = True
        for i in range(len(b)):
            if b[i] > x:
                b.remove(b[i])
                won = False
                break
        if won:
            b.remove(b[0])
            res_usual += 1
    print('{} {}'.format(war, res_usual))