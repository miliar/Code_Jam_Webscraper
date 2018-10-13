import sys


def foo():
    A, B = [int(x) for x in sys.stdin.readline().split()]
    counter = 0
    for n in range(A, B):
        register = {}
        for m in permut(n):
            if n < m and m <= B and m not in register:
                register[m] = True
                counter += 1
    return counter

def permut(num):
    s = str(num)
    l = len(s)
    for n in range(1, l):
        mv = s[l-n:l]
        if mv[0] != '0':
            for i in range(1, l-n+1):
                yield int(mv + s[0:l-n])


def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        print "Case #%s: %s" % (i+1, foo())

if __name__ == '__main__':
    main()


