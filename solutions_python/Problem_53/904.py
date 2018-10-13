import sys
import os

os.chdir("/Users/nolze/Desktop")

fi = open("input.txt", 'r')
sys.stdin = fi

fo = open("output.txt", 'w')
sys.stdout = fo

for cs in range(input()):
    c = map(int, raw_input().split())
    s = [1]
    t = [1]

    for k in range(c[0]):
        s.append(0)
        t.append(0)
    
    for n in range(c[1]):
        #Scan
        for i in range(1, len(s)):
            if(s[i-1] == 1):
                if(s[i] == 0): t[i] = 1
                else: t[i] = 0
            else:
                t[i:] = s[i:]
                break
        s = t[:]
    if((0 in s) == False): print "Case #" + str(cs+1) + ": ON"
    else: print "Case #" + str(cs+1) + ": OFF"
