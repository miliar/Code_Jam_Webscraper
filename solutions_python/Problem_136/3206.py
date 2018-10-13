#### Problem B. Cookie Clicker Alpha ####

from math import floor


# input
filename = "input"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')

# test case loop
for caseIdx in range(T):
    [C, F, X] = map(float, lines.__next__().split(' '))

    rmax = ((X-C)*F)/C                  # objective cookie rate
    upgrades = floor((rmax-2)/F)        # number of upgrades necessary to achieve rmax (maybe one more...)

    r = 2                               # initial rate
    t = 0                               # time consumed
    while upgrades>0:
        t += C/r                        # time before being able to upgrade
        r += F                          # upgrade!
        upgrades -= 1                   # upgrade!
    t += min(X/r, C/r + X/(r+F))        # time necessary to complete


    # print output
    msg = ("%.7f" % t)
    out = 'Case #' + str(caseIdx + 1) + ': ' + msg + '\n'
    output.write(out)
    # print(out)

output.close()
print(open('output', 'r').read())
