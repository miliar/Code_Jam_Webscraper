import sys

def read_lawn(input):
    n, _m = map(int, next(input).split())
    return [map(int, next(input).split())
            for _ in range(n)]

def possible(lawn):
    row_heights = [max(row) for row in lawn]
    col_heights = [max(col) for col in zip(*lawn)]
    mowed = [[min(r, c) for c in col_heights]
             for r in row_heights]
    ## print "\n".join(" ".join(map(str,row)) for row in lawn)
    ## print
    ## print "\n".join(" ".join(map(str,row)) for row in mowed)
    ## print "\n".join(" ".join(map(str,row)) for row in lawn) == "\n".join(" ".join(map(str,row)) for row in mowed)
    return lawn == mowed


def main(input):
    for i in range(int(next(input))):
        print 'Case #%d: %s' % (i+1, ['NO', 'YES'][possible(read_lawn(input))])


if __name__ == '__main__':
    input = open(sys.argv[1])
    main(input)
