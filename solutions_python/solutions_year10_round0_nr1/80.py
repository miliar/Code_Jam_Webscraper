import sys

def solve(n, k):
    return "ON" if k % (2 ** n) == (2 ** n - 1) else "OFF"

def main():
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        n, k = [int(x) for x in sys.stdin.readline().strip().split()]
        print "Case #%d: %s" % (i +1, solve(n, k))

if __name__ == "__main__":
    main()
