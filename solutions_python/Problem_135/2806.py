import sys


def solver(f):
    cases = int(f.readline().strip())
    for i in range(cases):
        q1 = int(f.readline().strip())
        rows = []
        for x in range(4):
            items = f.readline().split()
            rows.append(set(items))
        round1 = rows[q1 -1]

        q2 = int(f.readline().strip())
        rows = []
        for x in range(4):
            items = f.readline().split()
            rows.append(set(items))

        round2 = rows[q2 -1]

        result = round1.intersection(round2)

        if len(result) == 1:
            print "Case #%d: %s" % (i + 1, result.pop())

        elif len(result) > 1:
            print "Case #%d: Bad magician!" % (i + 1)

        else:
            print "Case #%d: Volunteer cheated!" % (i + 1)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        solver(f)

