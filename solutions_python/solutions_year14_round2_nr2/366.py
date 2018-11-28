#! /usr/bin/python

def solve(a, b, k):
    # go brute or go home
    return sum(1
               for aa in xrange(a)
               for bb in xrange(b)
               if aa & bb < k)


def main():
    t = input()
    for i in xrange(1, t + 1):
        a, b, k = map(int, raw_input().split())
        print 'Case #{0}: {1}'.format(i, solve(a, b, k))


if __name__ == '__main__':
    main()
