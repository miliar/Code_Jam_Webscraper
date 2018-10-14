import math
testcases = int(input())
for i in range(1, testcases+1):
    r, t = input().split()
    r = int(r)
    t = int(t)
    b = 2*r - 1
    sol = int((((math.sqrt( b*b + 8*t)) - b)/4))
    if(2*sol*sol + 2*sol*r - sol > t): sol-=1
    print("Case #"+str(i)+": "+str(int(sol))) 