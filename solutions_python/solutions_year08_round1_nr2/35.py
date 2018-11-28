import sys
    
def _copy(fixed,cs):
    cs_=[]
    for c in cs:
        cs_.append(c.copy())
    
    return (fixed.copy(),cs_)

def _reduce(fixed,cs_curr):
    cs_prev=None
    while cs_curr!=[]:
        cs_next=[]
        for c in cs_curr:
            if len(c)==0:
                return None
            elif len(c)==1:
                k=c.keys()[0]
                v=c.values()[0]
                
                if k in fixed:
                    if fixed[k]!=v: return None
                else:
                    fixed[k]=v
            else:
                cs_next.append(c)
        
        # mask
        cs_curr=cs_next
        cs_next=[]
        fks=fixed.keys()
        for c in cs_curr:
            for fk in fks:
                if fk in c:
                    if c[fk]==fixed[fk]: # satisfied
                        break
                    else:
                        del c[fk]
            else:
                cs_next.append(c)
        cs_curr=cs_next
        
        if cs_curr==cs_prev: break
        cs_prev=cs_curr
    
    return (fixed,cs_curr)

def _eval(fixed):
    return sum(map(int,fixed.values()))

def _search(fixed,cs):
    x=_reduce(fixed,cs)
    if x==None: return None
    fixed,cs=x
    if cs==[]: return fixed    
    
    rs=[]
    for k in cs[0].keys():
        assert k not in fixed
        
        fx2,cs2=_copy(fixed,cs)
        fx2[k]=cs[0][k]
        fx2=_search(fx2,cs2)
        
        if fx2!=None:
            rs.append((_eval(fx2),fx2))
    
    if rs==[]: return None
    
    rs=min(rs)
    return rs[1]
    
        
    
def _expand(cs):
    branch=True
    
    cs2_f=[]
    cs2_t=[]
    for c in cs:
        d={}
        for (k,v) in c.items():
            if branch and v=='both':
                d_t=d.copy()
                d[k]=False
                d_t[k]=True
        
                cs2_f.append(d)
                cs2_t.append(d_t)
                branch=False
            else:
                d[k]=v        
                cs2_f.append(d)
                cs2_t.append(d)
    
    if branch:
        return [cs2_f]
    else:
        return _expand(cs2_f)+_expand(cs2_t)
            

def proc_case():
    # parse
    n_flavors=int(sys.stdin.readline())
    n_customers=int(sys.stdin.readline())

    cs=[]
    for i in range(n_customers):
        xs=map(int,sys.stdin.readline().split())

        d={}
        for j in range(xs[0]):
            k=xs[1+j*2]-1
            v=(xs[2+j*2]==1)
            if k in d:
                d[k]='both'
            else:
                d[k]=v
        
        cs.append(d)
    
    # expand
    css=_expand(cs)
    assert len(css)==1
    
    # search
    results=[]
    for cs0 in css:
        fixed=_search({},cs)
        if fixed!=None:
            results.append((_eval(fixed),fixed))

    if results==[]:
        return 'IMPOSSIBLE'
    fixed=min(results)[1]
    
    # fill in the rest
    for i in range(n_flavors):
        if i not in fixed: fixed[i]=False
    
    #
    s=' '.join(map(lambda i:'1' if fixed[i] else '0',range(n_flavors)))
    return s

def proc_all():
    n_case=int(sys.stdin.readline().rstrip())
    for i in range(n_case):
        print 'Case #%d: %s'%(i+1,proc_case())
    

proc_all()
    

