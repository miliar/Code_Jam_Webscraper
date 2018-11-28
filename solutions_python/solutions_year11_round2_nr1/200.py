from __future__ import division
import sys

lines = sys.stdin.readlines()
lines = map(lambda a:a.rstrip('\n'), lines)
#print lines

def getWP(s):
    match = 0
    win = 0
    for c in s:
        if c=='1':
            win += 1
            match += 1
        if c=='0':
            match += 1
    return win/match
    
T = int(lines[0])
index = 0
for i in range(T):
    print "Case #%d:" % (i+1)
    index += 1
    N = int(lines[index])
    s_list = []
    for j in range(N):
        index += 1
        s_list.append(lines[index])
    
    # WP
    WP = []
    for s in s_list:
        WP.append(getWP(s))
        
    # OWP
    OWP = []
    for out in range(N):
        s = s_list[out]
        tmp_list = []
        for j in range(len(s)):
            if s[j]=='.':
                continue
            tmp = s_list[j][:]
            tmp = tmp[0:out]+tmp[out+1:]
            tmp_list.append(getWP(tmp))
        OWP.append(sum(tmp_list)/len(tmp_list))
    
    # OOWP
    OOWP = []
    for out in range(N):
        s = s_list[out]
        tmp_list = []
        for j in range(len(s)):
            if s[j]=='.':
                continue
            tmp_list.append(OWP[j])
        OOWP.append(sum(tmp_list)/len(tmp_list))
        
    # ans
    for j in range(N):
        print 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j]