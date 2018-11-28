from os import sys
sys.setrecursionlimit(50000)

def solve(pancake):
    #print "in\t\t",pancake

    top = 10
    while(pancake[top] == 0 and top >= 0):
        top -= 1

    if(top <= 3):
        return top

    pancake2 = dict(pancake)
    for i in range(1,10):
        pancake2[i] = pancake2[i+1]
    pancake2[10] = 0
    #print "eat\t\t",pancake2
    tmp = solve(dict(pancake2)) + 1

    for i in range(1,top):
        pancake3 = dict(pancake)
        pancake3[i] += pancake[top]
        pancake3[top-i] += pancake[top]
        pancake3[top] = 0
        #print "special," + str(i) + "\t",pancake3
        tmp = min(tmp,solve(dict(pancake3)) + pancake[top])
    return tmp

T = int(raw_input().strip())

for test in range(1,T+1):
    D = int(raw_input().strip())
    p = raw_input().strip().split()
    for i in range(D):
        p[i] = int(p[i])

    pancake = {}
    for i in range(11):
        pancake[i] = 0
    for i in p:
        pancake[i] += 1
    ans = solve(dict(pancake))
    print "Case #" + str(test) + ": " + str(ans)
