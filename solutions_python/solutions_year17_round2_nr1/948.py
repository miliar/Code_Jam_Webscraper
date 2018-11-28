def solve():
    dest, N = map(int, raw_input().split(" "))
    slowest = 0
    for x in xrange(N):
        pos, speed = map(int, raw_input().split(" "))
        t = (dest - pos)/float(speed)
        if t > slowest:
            slowest = t

    return dest/slowest


def main():
    numTest = int(raw_input())
    for testNum in xrange(1, numTest + 1):
        print "Case #{}: {:.6f}".format(testNum, solve())

if __name__ == '__main__':
    main()