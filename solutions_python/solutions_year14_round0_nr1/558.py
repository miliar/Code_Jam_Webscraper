import sys

def handle_test(num, f):
    line1 = handle_question(f)
    line2 = handle_question(f)
    numbers = line1 & line2
    if len(numbers) > 1:
        print "Case #%d: Bad magician!"%num
    if len(numbers) < 1:
        print "Case #%d: Volunteer cheated!"%num
    if len(numbers) == 1:
        print "Case #%d: %d"%(num, numbers.pop())


def handle_question(f):
    ans = int(f.readline().strip())
    for j in xrange(4):
        row = f.readline()
        if j + 1 == ans:
            line = set([int(x) for x in row.split()])
    return line

f = open(sys.argv[1])
cases = int(f.readline().strip())
for i in xrange(cases):
    handle_test(i + 1, f)


