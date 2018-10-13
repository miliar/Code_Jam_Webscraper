import numpy as np
import scipy
import math


nt = int(raw_input())

def max_idx(l,f):
    mxi = -1
    mx = None
    
    for i in xrange(len(l)):
        if i == f:
            continue
        if mxi == -1 or l[i] > mx:
            mx = l[i]
            mxi = i
    return mxi

def solve(lt):
    
    v = [t[0] for t in lt]
    sv = sum(v)
    
    if min(v) < 0:
        return False,[]
    
    if 2*(max(v)) > sv:
        return False,[]
    
    cur = -1
    ans = []
    while len(ans) < sv:
        imx = max_idx(v,cur)
        if imx < 0: return []
        
        ans.append(lt[imx][1])
        v[imx] -= 1
        cur = imx
    
    return True,ans
        
    
for i_it in xrange(nt):
    n,r,o,y,g,b,v = map(int, raw_input().split())
    
    lt = [[(r-g),'R'],[(y-v),'Y'],[(b-o),'B']]
    
    mv = {'R' : g , 'Y' : v , 'B' : o}
    mc = {'R' : 'G' , 'Y' : 'V' , 'B' : 'O'}
    
    #print lt
    ok,ans = solve(lt)
    
    if ok and len(ans) > 2 and ans[0] == ans[-1]:
        tmp = ans[-1]
        ans[-1] = ans[-2]
        ans[-2] = tmp
        
    for pc in ['R','Y','B']:
        if mv[pc] == 0: continue
        ipc = 0
        while ipc < len(ans):
            if ans[ipc] == pc:
                break
            ipc += 1
            
        if ipc < len(ans):
            ans[ipc] = pc + (mc[pc]+pc)*mv[pc]
        else:
            if len(ans) > 0:
                ok = False                
            else:
                ans = (pc+mc[pc])*mv[pc]                
            break
    
    str_ans = 'IMPOSSIBLE' if not ok else ''.join(ans)    
    print "Case #{}: {}".format(i_it+1,str_ans)
    
