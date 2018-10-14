import sys
import re


def main(ifile):
    L,D,N = [int(x) for x in ifile.readline().split()]
    a = [ifile.readline().strip() for i in range(D)]
    b = [ifile.readline().strip() for i in range(N)]
    b = [x.replace('(', '[').replace(')', ']') for x in b]
    b = [re.compile(x) for x in b]

    for i in range(len(b)):
        print 'Case #%d: %d' % (i+1, len([x for x in a if b[i].match(x)]))
    


if __name__ == '__main__':
    main(sys.stdin)
