# Google Code Jam 2011 Round 1A
# Cole Gleason -- cg@colegleason.com

import sys
input = [x.rstrip('\n') for x in sys.stdin.readlines()]
answers = []
cases = []

T = int(input[0])

for x in range(1,T + 1):
    cases.append(map(int, input[x].split(' ')))
    cases[x - 1][1] = cases[x - 1][1] / 100.0
    cases[x - 1][2] = cases[x - 1][2] / 100.0

for case in cases:
    D = []
    for i in range(1, case[0] + 1):
        d = (case[1] * i)
        if  d.is_integer():
                D.append((i,int(d)))

    if (case[2] == 1.0) and (case[1] != 1.0):
        answers.append('Broken')
    elif (case[2] == 0.0) and (case[1] != 0.0):
        answers.append('Broken')
    elif D == []: answers.append('Broken')
    else: answers.append('Possible')


for x in range(0, len(answers)):
    print "Case #%d: %s" % (x+1, answers[x])
