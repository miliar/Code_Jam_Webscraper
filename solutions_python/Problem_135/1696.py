import sys


def foo(ifile):
    n1 = int(ifile.readline().strip())
    a1 = [[int(x) for x in ifile.readline().split()] for i in range(4)]
    b1 = set(a1[n1-1])
    n2 = int(ifile.readline().strip())
    a2 = [[int(x) for x in ifile.readline().split()] for i in range(4)]
    b2 =set(a2[n2-1])
    res = b1.intersection(b2)
    if len(res) == 1:
        return list(res)[0]
    if len(res) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

