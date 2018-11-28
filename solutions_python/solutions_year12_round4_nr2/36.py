import random
import math
import time
def check(circles):
    for i in range(len(circles)):
        for j in range(len(circles)):
            if i!=j :
                a = circles[i]
                b = circles[j]
                if math.sqrt((a[0]-b[0])**2 +(a[1]-b[1])**2) <= a[2]+b[2]:
                    return False
    return True
def generate(n,radii,w,l):
    return [(random.randint(0,w),random.randint(0,l),radii[i]) for i in range(n)]
t = int(raw_input())

for tt in range(1,t+1):
    line = raw_input().strip().split()
    n = int(line[0])
    ww = int(line[1])
    l = int(line[2])
    line = raw_input().strip().split()
    radii = [int(i) for i in line]
    w = False
    circles=[]
    while not w:
        circles = generate(n,radii,ww,l)
        w = check(circles)
    res = "Case #{}: ".format(tt)
    for i in circles:
        res+=str(i[0])+" "+str(i[1])+" "
    print res
