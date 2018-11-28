import math
import sys


def read_inputs(filename):
    f = open(filename, 'rt')

    inputs = []
    count = int(f.readline())

    for c in xrange(count):
        sizes = [int(x) for x in f.readline().split(' ')]
        inputs.append((sizes[0], sizes[1]))

    f.close()
    return inputs

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def main():
    inputs = read_inputs(sys.argv[1])

    idx = 1
    for (a, b) in inputs:
        print 'Case #{}:'.format(idx),

        count = 0
        for z in xrange(a, b + 1):
            if not is_palindrome(z):
                continue

            root = int(math.sqrt(z))

            if root * root != z:
                continue

            if not is_palindrome(root):
                continue

            count += 1

        print count

        idx += 1

if __name__ == '__main__':
    main()
