__author__ = 'thainguyen'

# fi = open('StandingOvation.in', 'r')
# fi = open('A-small-attempt0.in','r')
fi = open('A-large.in','r')
fo = open('StandingOvation.out', 'w')

tests = int(fi.readline())
for test_case in range(tests):
    line = fi.readline()
    s = int(line.split()[0])
    audiences = line.split()[1]
    curr = 0
    res = 0
    for i in range(s+1):
        if curr >= i:
            curr += int(audiences[i])
        else:
            res += i - curr
            curr = i + int(audiences[i])
    fo.write('Case #' + str(test_case+1) + ': ' + str(res)+'\n')