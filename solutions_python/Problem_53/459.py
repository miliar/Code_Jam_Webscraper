import sys

if __name__ == '__main__':
    s = sys.stdin.readline()

    for i in range(1, int(s) + 1):
        line = sys.stdin.readline()
        n, k = line.split()
        n = int(n)
        k = int(k)

        p = (2 ** n)

        l = k % p
        if l == p - 1:
            r = 'ON'
        else:
            r = 'OFF'

        print("Case #%d: %s" % (i, r))
