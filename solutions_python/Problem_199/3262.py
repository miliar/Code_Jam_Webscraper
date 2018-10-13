import sys


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        pancakes, k = raw_input().split(" ")
        k = int(k)
        pancakes = list(pancakes)
        m = 0
        nr_flips = 0
        while m < len(pancakes):
            if pancakes[m] == '-':
                if m + k <= len(pancakes):
                    nr_flips += 1
                    steps = None
                    for n in range(k):
                        new_side = '-' if pancakes[m+n] == '+' else '+'
                        pancakes[m+n] = new_side
                        if steps is None and new_side == '-':
                            steps = n
                    if steps:
                        m += steps
                    else:
                        m += k
                else:
                    nr_flips = 'IMPOSSIBLE'
                    break
            else:
                m += 1
        print "Case #%d: %s" % (i, nr_flips)

