import random

import sys

sys.setrecursionlimit(20000)

def minuses(signs, start):
    count = 0
    for i in range(start,len(signs)):
        x = signs[i]
        if x == "-":
            count += 1    
    return count

def solve(signs,k, start):
    counter = 0    
    if len(signs) - start < k:
        if minuses(signs, start) == 0:
            return 0
        else:
            return "IMPOSSIBLE"
    elif len(signs) - start == k:
        minus = minuses(signs, start)
        if minus == 0:
            return 0
        elif minus == k:
            return 1
        else:
            return "IMPOSSIBLE"

    else:
        if signs[start] == "+":
            for i in range(start, len(signs)):
                if signs[i] == "-":
                    ans = solve(signs, k, i)
                    return ans
            return 0
        else:
            new_start = start + k
            for i in range(start, start+k):
                if signs[i] == "+":
                    new_start = i
                    for j in range(i, start+k):
                        #print j, signs[j]
                        if signs[j] == "+":
                            signs[j] = "-"
                        else:
                            signs[j] = "+"
                        #print signs
                    break
            ans = solve(signs, k, new_start)
            if ans == "IMPOSSIBLE":
                return ans
            else:
                return ans+1

f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):

    #read input
    ss,k = [y for y in f.readline().split('\n')[0].split(' ')]
    k = int(k)
    s = [x for x in ss]

    #solve
    ans = solve(s,k,0)
    pr = "Case #"+str(i)+ ": " + str(ans)
    #print pr
    g.write(pr + '\n')


f.close()
g.close()

##for t in range(100):        
##    a = ""
##    for x in range(1000):
##        x = random.randint(0,1)
##        if x == 0:
##            a += "+"
##        else:
##            a += "-"
##
##    s = [x for x in a]
##    k = random.randint(1,1000)
##
##    print solve(s,k,0)
