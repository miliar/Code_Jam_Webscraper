
import itertools

def main():
    f = open('B-large.in')
#    f = sys.stdin
    tnum = int(f.readline())
    for t in range(1, tnum + 1):
        c, d, x = [float(x) for x in f.readline().split()]
        best = x / 2
        total = 0
        for n in itertools.count(1,1):
            total += c / (2 + d * (n - 1))
            cur = total + x / (2 + d * n)
            if cur > best:
                break
            best = cur
        print "Case #%d: %.7f" % (t, best)


if __name__ == "__main__":
    main()
