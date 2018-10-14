# -*- coding: utf-8 -*-
from __future__ import division

fname = "A-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

for caseno in range(numcases):
    L, S, R, t, N = gcj_read()
    walkways = (gcj_read() for _ in range(N))
    segments = []
    pos = 0
    for begin, end, v in walkways:
        if begin > pos:
            segments.append((begin - pos, 0))
        segments.append((end - begin, v))
        pos = end
    if L > pos:
        segments.append((L - pos, 0))
        
    segments.sort(key=lambda x: x[1])
    segments.reverse()
    
    t_orig = t
    while segments:
        d, v_add = segments.pop()
        Trun = d / (R + v_add)
        if t < Trun:
            got = (R + v_add) * t
            Twalk = (d - got) / (S + v_add)
            elapsed = t_orig + Twalk
            break
        else:
            t -= Trun
    else:
        # Got there while still running
        elapsed = t_orig - t
    
    # Walk any remaining segments:
    for d, v_add in segments:
        elapsed += d / (S + v_add)
            
    outstr = str(elapsed)
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
