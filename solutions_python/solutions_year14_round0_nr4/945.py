# Google Code Jam 2014 - Deceitful War
# Guy Weizman

import sys

__author__ = 'Guy Weizman'


# Calculates the maximum score naomi can achieve if ken plays the best he can
def war(length, naomi, ken):
    naomi = list(naomi)
    ken = list(ken)
    score = 0
    while len(naomi) > 0:
        for num in ken:
            if num > naomi[-1]:
                ken.remove(num)
                naomi.remove(naomi[-1])
                break
        else:
            score += 1
            naomi.remove(naomi[-1])
            ken.remove(ken[0])
            continue
    return score

# Calculates the maximum score naomi can achieve if ken plays the best he can and naomi deceives him
def deceitful(length, naomi, ken):
    naomi = list(naomi)
    ken = list(ken)
    score = 0
    while len(naomi) > 0:
        for num in naomi:
            if num > ken[-1]:
                score += 1
                naomi.remove(num)
                ken.remove(ken[-1])
                break
        else:
            naomi.remove(naomi[0])
            ken.remove(ken[-1])
            continue
    return score

if len(sys.argv) != 2:
    print 'Syntax: python cookie.py FILE_PATH [Without .in]'
    exit()

file = sys.argv[1]

readFile = open(file + '.in', 'r')
writeFile = open(file + '.out', 'w')

testCases = int(readFile.readline())

for i in range(testCases):
    length = int(readFile.readline())
    naomi = sorted(readFile.readline().split())
    ken = sorted(readFile.readline().split())
    writeFile.write("Case #" + str(i + 1) + ": " + str(deceitful(length, naomi, ken)) + " "
                    + str(war(length, naomi, ken)) + "\n")