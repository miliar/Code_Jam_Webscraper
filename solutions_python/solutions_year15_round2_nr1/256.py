import sys
import math


N = 10**6 + 1

def min_numbers(n):
    a = list(range(N))
    for i in range(2, N):
        x = a[i]
        reversed_str = ''.join(reversed(str(x)))
        r = int(reversed_str)
        if r < N and a[r] < a[i] and len(str(r)) >= len(str(x)):
            a[i] = min(a[i - 1] + 1, a[r] + 1)
        else:
            a[i] = a[i - 1] + 1
            # print ('-', n, x, r)


    # print (list(enumerate(a)))
    return a[n]

def main():
    t = int(sys.stdin.readline())
    for r in range(t):
        n = int(sys.stdin.readline())
        print ('Case #%d: %d' % (r + 1, min_numbers(n)))

if __name__ == '__main__':
    main()
