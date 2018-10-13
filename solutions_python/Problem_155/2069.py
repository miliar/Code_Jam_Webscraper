__author__ = 'jdr'

import sys

file = open(sys.argv[1], 'r')
f = open('sol.out','w')
i = 0

for line in file:
    line = line.strip()
    if i == 0:
        testcases = int(line)
    else:
        splited = line.split()
        smax = splited[0]
        digits = splited[1]

        j = 1
        standup = int(digits[0])

        if standup == 0:
            toadd = 1
            standup = 1
        else:
            toadd = 0

        while j <= int(smax):
            if int(digits[j]) > 0:
                if standup < j:
                    toadd += j - standup
                    standup += j - standup + int(digits[j])
                else:
                    standup += int(digits[j])
            j += 1

        f.write("Case #%d: %d\n" % (i, toadd))

    i += 1
f.close()
file.close()
