def process(tc):
    row1 = int(raw_input())
    matrix1 = [[int(n) for n in raw_input().split()] for i in xrange(4)]
    candidates = set(matrix1[row1 - 1])
    row2 = int(raw_input())
    matrix2 = [[int(n) for n in raw_input().split()] for i in xrange(4)]
    candidates = candidates & set(matrix2[row2 - 1])
    if not candidates:
        print "Case #%d: Volunteer cheated!" % tc
    elif len(candidates) == 1:
        print "Case #%d: %d" % (tc, list(candidates)[0])
    else:
        print "Case #%d: Bad magician!" % tc

if __name__ == "__main__":
    cases = int(raw_input())
    for tc in xrange(1, cases + 1):
        process(tc)
