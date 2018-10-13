import sys

num_cases = int(sys.stdin.readline())

def test_line(line, shortest):
    for e in line:
        if e != shortest:
            return False
    return True

def mow_lawn(lawn):
    if not lawn:
        return True
    shortest = min(min(lawn))
    for i, row in enumerate(lawn):
        if shortest in row:
            j = row.index(shortest)
            col = [e[j] for e in lawn]
            if test_line(row, shortest):
                lawn.pop(i)
                return mow_lawn(lawn)
            elif test_line(col, shortest):
                for row in lawn:
                    row.pop(j)
                return mow_lawn(lawn)
            else:
                return False

for n in xrange(num_cases):
    N, M = [int(e) for e in sys.stdin.readline().strip().split()]

    lawn = []
    for i in xrange(N):
        row = [int(e) for e in sys.stdin.readline().strip().split()]
        lawn.append(row)

    print "Case #%s: %s" % (n+1, "YES" if mow_lawn(lawn) else "NO")
    n += 1
