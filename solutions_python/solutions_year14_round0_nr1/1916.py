__author__ = 'Ricsipi'


f = open('a.in', 'r')
out = open('a.out','w')
n = int(f.readline())
print(n)

for i in range(n):
    row_n = int(f.readline())
    for r in range(4):
        line = f.readline()
        if r+1 == row_n:
            first = set(map(int, line.split()))
            print(first)

    # second
    row_n = int(f.readline())
    for r in range(4):
        line = f.readline()
        if r+1 == row_n:
            second = set(map(int, line.split()))
            print(second)
            result = first & second
            print("Final %s" % result)
            if len(result) == 1:
                out.write('Case #%d: %d\n' % (i+1, result.pop()))
            elif len(result) > 1:
                out.write('Case #%d: Bad magician!\n' % (i+1))
            else:
                out.write('Case #%d: Volunteer cheated!\n' % (i+1))

f.close()
out.close()