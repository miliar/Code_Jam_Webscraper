import sys

PALINS = [i**2 for i in range(1, int(1e7)+1) if str(i) == str(i)[::-1] and str(i**2)==str\
(i**2)[::-1]]


def main(input):
    for i in range(int(next(input))):
        a, b = map(int, next(input).split())
        print 'Case #%d: %s' % (i+1, sum(1 for p in PALINS if a<=p<=b))
#    test_cases = [lines[i*4for i in range(cases)]


if __name__ == '__main__':
    input = open(sys.argv[1])
    main(input)
