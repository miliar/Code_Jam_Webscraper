import math


def repeatNumber(m,n):
    #print "handed m=%s  n=%s" % (m, n)
    length = len(m)
    for i in range(0, length):
        newN = sum([n[i:length], n[0:i]],[])
        #print "comparing m=%s  n=%s" % (m, newN)
        if newN == m: return True

def countCases(A,B):
    count = 0
    #print "Comparing "+str(A)+" and "+str(B)
    for i in range(A,B):
        base = list(str(i))
        #print "Base is "+str(base)
        l1 = len(base)
        s1 = sorted(base)
        for j in range(i+1,B):
            compare = list(str(j))
            #print "Compare is "+str(compare)
            l2 = len(compare)
            if l2 != l1: continue
            #print "Lengths Match %d %d" % (l2, l1)
            s2 = sorted(compare)
            if s1 != s2: continue
            #print "pass sorted compare s1=%s  s2=%s" % (s1, s2)
            if repeatNumber(base,compare):
                count+=1
                #print "Match"
    return count

directory = "/home/se/Downloads/"

inFile=directory+"C-small-attempt0.in"
outfile = directory+"test.out"

input = open(inFile)
output = open(outfile, "w")

line = input.readline().strip()
cases = int(line)

for case in range(0,cases):
    numbers = input.readline().strip().split(' ')
    #print numbers
    matches = countCases(int(numbers[0]), int(numbers[1])+1)
    print >> output, "Case #%d: %d" % (case+1, matches)
    print "Case #%d: %d" % (case+1, matches)
