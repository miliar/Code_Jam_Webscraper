
# -*- coding: cp932 -*-

import sys

def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def main(s):
    
    ind = [0 for i in range(len(s))]
    ans = 0
    while(True):
        c = s[0][ind[0]]
        csum = 0
        ccount = [0 for i in range(len(s))]
        for i in range(len(s)):
            while ((ind[i] < len(s[i])) and (s[i][ind[i]] == c)):
                ind[i] += 1
                ccount[i] += 1
                csum += 1
            if ccount[i] == 0:
                return "Fegla Won"
        
        avg = round(csum/len(s))
        for i in range(len(s)):
            ans += abs(ccount[i] - avg)


        if (ind[0] == len(s[0])):
            for i in range(len(s)):
                if (ind[i] != len(s[i])):
                    return "Fegla Won"
            
            break
            
    return str(ans)

inputfile = "A-small-attempt0.in"
f = open(inputfile)
sys.stdout = open(inputfile.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    N = int(f.readline().rstrip())
    s = []
    for i in range(N):
        s.append(f.readline().rstrip())
    
    ans = main(s)
    debug(str(tc))
    print("Case #" + str(tc+1) + ": " + ans)

   
