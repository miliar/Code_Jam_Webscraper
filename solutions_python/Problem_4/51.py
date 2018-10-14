from string import *

inn = open('input.txt', 'r')
def getz():
    global inn
    return inn.readline().strip()
outt = open('output.txt','w')

testt = int(getz())

for testcase in range(testt):
    n = int(getz())
    a = map(int,getz().split())
    b = map(int,getz().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        ans += a[i]*b[-1-i]
    print "%s%d%s%d" % ("Case #",testcase+1,": ",ans)
