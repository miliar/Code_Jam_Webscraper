import sys
sys.setrecursionlimit(1500)

def min_frnds(last_s):
    if last_s == 0:
        return aud_dic[last_s], 0
    total_frnds, total_extra = min_frnds(last_s-1)
    extra = 0
    if total_frnds < last_s:
        extra = last_s - total_frnds
        aud_dic[0] += extra
    total_frnds += aud_dic[last_s] + extra
    total_extra += extra 
    return total_frnds, total_extra

cases = int(raw_input())
for case in range(cases):
    print "Case #%s:" % (case+1),
    line1 = raw_input().split()
    last_s = int(line1[0])
    auds = line1[1]
    global aud_dic
    aud_dic = {}
    for i, a in enumerate(auds):
        aud_dic[i] = int(a)
    print min_frnds(last_s)[1]
    
