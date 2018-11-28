'''
Created on Apr 14, 2012

@author: lucamaf
'''

def comp_rec(a,b):
    result=0
    l=[]
    for i in range(a,b+1):
        n=str(i)
        lenn=len(n)
        #if n[lenn-1]!='0':
        for i in range(lenn):
            m=n[i+1:]+n[:i+1]
            mnum=int(m)
            mnums=str(mnum)
            if mnum<=b and len(mnums)==lenn and [n,m] not in l and [m,n] not in l and m>n:
                result+=1
                l.append([n,m])
    #print l
    return result

def results(afile):
    f=open(afile)
    case=int(f.next())
    for i in range(case):
        line=f.next()
        nums=line.split()
        a=int(nums[0])
        b=int(nums[1])
        res=comp_rec(a, b)
        print 'Case #{case}: {s}'.format(case=i+1,s=res)

results('C-small-attempt0.in.txt')