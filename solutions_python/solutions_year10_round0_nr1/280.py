
import sys


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        N, K = map(int, line.split())

        power = 2 ** N
        res = 'ON' if (K % power) == (power - 1) else 'OFF'

        print "Case #%d: %s" % (i+1, res)

