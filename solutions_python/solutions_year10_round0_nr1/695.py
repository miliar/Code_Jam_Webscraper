import sys

def next_line():
    return sys.stdin.readline()

def run():
    n, k = next_line().split()
    n, k = int(n), int(k)

    a = 2**n
    if (k+1) % a == 0:
        return u'ON'
    return u'OFF'

def main():
    n = int(next_line())

    for nr in range(1,n+1):
        print "Case #%d: %s" % (nr, run())

main()
