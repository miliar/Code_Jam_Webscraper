import sys

def line():
    return sys.stdin.readline().strip()

def ints(s):
    return [int(t) for t in s.split()]

def answer(common):
    ln = len(common)
    if ln == 0:
        return 'Volunteer cheated!'
    elif ln == 1:
        return str(common.pop())
    else:
        return 'Bad magician!'


def main():
    tc = int(line())
    for i in range(1,tc+1):
        a1 = int(line())
        grid1 = []
        for j in range(4):
            grid1.append(set(ints(line())))
        a2 = int(line())
        grid2 = []
        for j in range(4):
            grid2.append(set(ints(line())))

        common = grid1[a1-1] & grid2[a2-1]
        s = answer(common)

        print 'Case #%s: %s' % (i, s)

main()
