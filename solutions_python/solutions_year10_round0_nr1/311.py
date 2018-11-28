import sys

def foo():
    line = sys.stdin.readline()
    N, K = [int(x) for x in line.split()]

    t = 2 ** N
    #print N, K, t
    if (K+1) % t == 0:
        return "ON"
    else:
        return "OFF"


def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        print "Case #%s: %s" % (i+1, foo())


if __name__ == '__main__':
    main()
