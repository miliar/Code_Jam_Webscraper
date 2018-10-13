from sys import stdin
import collections
import functools

DEBUG = False


def debug_print(*args):
    if DEBUG:
        print args

def solved(pc):
    if pc == '+' * len(pc):
        return True

def swap(x):
    if x == '-':
        return '+'
    return '-'

def flip(pc, i, k):
    # print "flipping"
    # print pc, i, k
    if i + k > len(pc):
        raise Exception
    l = pc[:i]
    r = pc[i+k:]
    m = ''.join([swap(x) for x in pc[i:i+k]])
    # print l+m+r
    return l + m + r

def solve(pc, k):
    # print pc, k
    if solved(pc):
        return 0
    # print len(pc), k, len(pc) - k
    if len(pc) < k:
        return -1

    steps = 0
    # print (len(pc) - (k-1))
    for i in range(len(pc) - (k-1)):
        # print pc, i, k
        if pc[i] == '-':
            pc = flip(pc, i, k)
            steps += 1
        if solved(pc):
            return steps

    return -1


def main():
    num_cases = int(stdin.readline())
    for case in range(1, num_cases + 1):

        pc, k = stdin.readline().strip().split()
        k = int(k)

        n = solve(pc, k)

        if n == -1:
            n = "IMPOSSIBLE"

        print "Case #{}: {}".format(case, n)

if __name__ == "__main__":
    main()
