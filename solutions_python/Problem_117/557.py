def valid_cut(lawn, vert, horiz):
    for i, row in enumerate(lawn):
        for j, col in enumerate(row):
            if min([vert[j], horiz[i]]) != col:
                return False
    return True

def find_cut(lawn):
    nrow, ncol = len(lawn), len(lawn[0])

    vert = [max(l[i] for l in lawn) for i in range(ncol)]
    horiz = [max(l) for l in lawn]

    return valid_cut(lawn, vert, horiz)

def test():
    lawn = [[2, 1, 2], [1, 1, 1], [2, 1, 2]]
    assert find_cut(lawn)

    lawn = [[2, 2, 2, 2, 2],
            [2, 1, 1, 1, 2],
            [2, 1, 2, 1, 2],
            [2, 1, 1, 1, 2],
            [2, 2, 2, 2, 2]]

    assert not find_cut(lawn)

    lawn = [[1, 2, 1]]
    assert find_cut(lawn)


def main(fname):

    data = [d.strip() for d in open(fname + '.in')]
    outfile = open(fname + '.out', 'w')

    T = int(data[0])

    data = data[1:]
    for i in range(T):
        nrow, ncol = map(int, data[0].split())
        lawn = [map(int, row.split()) for row in data[1:1+nrow]]

        assert len(lawn[0]) == ncol

        result = "YES" if find_cut(lawn) else "NO"
        print "Case #%i: %s" % (i+1, result)
        outfile.write("Case #%i: %s\n" % (i+1, result))
        if i < (T - 1):
            data = data[1+nrow:]

    outfile.close()

if __name__ == "__main__":
    test()
    import sys
    main(sys.argv[1])
