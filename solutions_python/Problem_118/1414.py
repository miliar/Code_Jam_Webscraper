#run with "python2 problemC.py <inputfile >outputfile" on arch linux
import math

def p(numb):
    s = str(numb)
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

cases = input("")

for case in range(cases):
    count = 0
    borders = raw_input()
    bottom = int(math.sqrt(int(borders.split(" ")[0])))
    upper = int(borders.split(" ")[1])
    if (bottom)**2 != int(borders.split(" ")[0]):
        bottom += 1

    i = bottom
    
    while i**2 <= upper:
        if p(i) and p(i*i):
            count += 1
        i += 1
    print "Case #%s: %s" %(case+1, count)    
    
