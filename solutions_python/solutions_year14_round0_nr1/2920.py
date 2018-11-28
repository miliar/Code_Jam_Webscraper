import sys
T = int(sys.stdin.readline())

def read_row(row_index):
    r = None
    for i in xrange(4):
        line = sys.stdin.readline().strip()
        if i == row_index:
            r = map(int, line.split())
    return r

for t in xrange(T):
    first = read_row(int(sys.stdin.readline()) - 1)
    second = read_row(int(sys.stdin.readline()) - 1)
    common = list(set(first) & set(second))
    print "Case #{0}:".format(t + 1),
    if len(common) == 1:
        print common[0]
    elif len(common) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
