import os
import math
def ispalindrome(i):
    p = str(i)
    lenp = len(p)
    for j in xrange(lenp/2):
        if p[j] != p[lenp-j-1]:
            return False
    return True

def solve(a, b):
    i = a
    cnt = 0
    while (i <= b):
        if ispalindrome(i):
            j = math.sqrt(i)
            if j == int(j):
                j = int(j)
                if ispalindrome(j):
                    cnt += 1
        i += 1
    return cnt

### MAIN ###

os.chdir("D:/")
fd = open("C-small-attempt0.in", "rt")
out = open("output.txt", "w+t")
cases = int(fd.readline().rstrip('\n'))
for case in xrange(cases):
    interval = fd.readline().rstrip('\n').split(" ")
    for i in xrange(len(interval)):
        interval[i] = int(interval[i])
    nums = solve(interval[0], interval[1])
    out.write("Case #" + str(case+1) + ": " + str(nums) + "\n")
    
fd.close()
out.close()
