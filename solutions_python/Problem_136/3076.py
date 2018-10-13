from __future__ import division
import sys

def main():
    for i in range(10):
        pass
        #print buy_n(i, 30, 2, 100)
    f = open(sys.argv[1])
    num = int(f.readline())
    for i in range(num):
        print 'Case #%d: %.7f' % (i + 1, run(f))

def run(f):
    inputs = map(float, f.readline().split(' '))
    if inputs[2] < inputs[0]:
        return inputs[2] / 2
    n = get_n(inputs[0], inputs[1], inputs[2])
    result = min(buy_n(n, inputs[0], inputs[1], inputs[2]), buy_n(n + 1, inputs[0], inputs[1], inputs[2]))
    return result


def buy_n(n, c, f, x):
    total = 0
    if n <= 0:
        return x / 2
    for i in range(n):
        total += c / (2 + i * f)
    return total + x / (2 + n * f)

def get_n(c, f, x):
    result = x / c - 1 - 2 / f
    return int(result)

if __name__ == '__main__':
    main()
