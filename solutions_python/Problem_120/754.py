import math
def soln(r, t):
    count  = 0
    area = 2*r +1
    while(area <= t):
        t = t-area
        r  = r + 2
        area = 2*r+1
        count += 1
    print count
    return count

fi = open('input.in', 'r')
fo = open('output.out', 'w')
testcases = int(fi.readline())
caseNo = 0
for caseNo in range(1, testcases+1):
    count = 0
    r,t = fi.readline().split()
    r,t = int(r), int(t)
    ans = soln(r,t)
    fo.writelines('Case #'+str(caseNo)+': '+str(ans)+chr(10))
