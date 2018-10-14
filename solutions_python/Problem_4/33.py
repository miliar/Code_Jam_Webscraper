
def main(input):
    T = int(input.readline())
    for i in range(T):
        n = int(input.readline())
        x = [int(s) for s in input.readline().split()]
        y = [int(s) for s in input.readline().split()]
        assert len(x) == len(y) == n
        x.sort()
        y.sort(reverse=True)
        s = 0
        for j in range(n):
            s += x[j]*y[j]
        print "Case #%d:"%(i+1), s

if __name__ == '__main__':
    import sys
    f = sys.stdin
    #f = open('A.txt')
    main(f)
