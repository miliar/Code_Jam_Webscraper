#### Problem C. Fair and Square ####

from math import sqrt, ceil, floor


def fair(n):
    nstr = str(n)
    for i in range(ceil(len(nstr)/2)):
        if nstr[i] != nstr[len(nstr) - 1 - i]:
            return False
    return True

# input
filename = "C-small-attempt0.in"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')

# test case loop
for caseIdx in range(T):
    [a, b] = map(int, lines.__next__().split(' '))

    n = 0
    for i in range(ceil(sqrt(a)), floor(sqrt(b)) + 1):
        if fair(i) and fair(i*i):
            # print('(' + str(i) + ', ' + str(i*i) + ')')
            n += 1

    # print output
    msg = str(n)
    output.write('Case #' + str(caseIdx + 1) + ': ' + msg + '\n')

output.close()
print(open('output', 'r').read())
31
