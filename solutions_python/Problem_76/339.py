import sys

def solve(args):
    bins = [0] * 20
    minimum = 10**6 + 1
    minindex = -1
    for e in enumerate(args):
        a = e[1]
        if a < minimum:
            minimum = a
            minindex = e[0]
        dig = 0
        while a != 0:
            if (a & (1 << dig)) != 0:
                bins[dig] += 1
                a -= (1<<dig)
            dig += 1
    for b in bins:
        if (b & 1):
           return 'NO'
       
    result = 0
    assert minindex >= 0
    for e in enumerate(args):
        if e[0] != minindex:
            result += e[1]
    return str(result)


def main():
    f = open(sys.argv[1])
    n = int(f.next())
    for i in range(n):
        f.next()
        r = solve([int(a) for a in f.next().split()])
        print 'Case #%d: %s' % (i+1, r)
    

if __name__ == '__main__':
    main()
    