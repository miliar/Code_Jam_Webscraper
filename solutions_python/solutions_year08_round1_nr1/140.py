import sys

def read_case(lines):
    vec1 = [int(e) for e in lines[1].strip().split()]
    vec2 = [int(e) for e in lines[2].strip().split()]
    return vec1, vec2, lines[3:]

if __name__ == '__main__':
    lines = open(sys.argv[1]).readlines()[1:]
    caso = 0
    while lines != [] :
        caso += 1
        v1, v2, lines = read_case(lines)
        v1.sort()
        v2.sort()
        product = reduce(lambda a,b : a+b, [a*b for a,b in zip(reversed(v1),v2)], 0)
        print 'Case #%d:' % caso, product
