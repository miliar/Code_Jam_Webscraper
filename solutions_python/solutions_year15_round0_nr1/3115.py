from parse import *
f = open('input', 'r')

l=f.readline()
l=f.readline()
testcase_nb=0
while (l != ''):
    solution = 0
    testcase_nb+=1
    testcase = [s for s in l.split( ) if s.isdigit()]
    ch = testcase[1]
    audience = 0
    for i in range(0, int(testcase[0]) + 1):
        audience += int(ch[i])
        if (audience <= i):
            solution += 1
            audience += 1
    print("Case #" + str(testcase_nb) + ": " + str(solution))
    l=f.readline()
