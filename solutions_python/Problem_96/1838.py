import sys
file = sys.argv[1]
input = open(file,'r')

def getmin(p):
    if p == 0:
        return 0
    if p == 1:
        return 0
    return p * 3 -2

def getnewmin(p):
    if p == 0:
        return 0
    if p == 1:
        return 0
    return p * 3 -4





t = int(input.readline())
# there are n test cases, we will loop over t cases

for i in range(t):
    line = input.readline().split()
    g = int(line[0])
    s = int(line[1])
    p = int(line[2])
    t = line[3:]
    #print "there are ", g, " goolgers with " , s , " surprisings looking for " , p , " minimum with these scores " , t

    min  = getmin(p)
    
    answer = 0

    for j in t:
        if int(j) >= min and int(j) >= p:
            answer = answer + 1

#print "so far there are ", answer, " cases"

    if s > 0:
        newmin = getnewmin(p)
        for j in t:
            if int(j) < min and int(j) >= newmin and int(j) > p:
                answer = answer + 1
                s = s - 1
            if s == 0:
                break

    print "Case #" + str(i+1)+": " , answer
        