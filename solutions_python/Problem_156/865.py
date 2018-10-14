def go():
    f=open('in.txt')
    c=int(f.readline())
    for case in range(1,c+1):        
        print 'Case #%d:'%case,
        f.readline()
        print solve(f.readline())
    f.close()

def minusone(x):
    if x==0:
        return 0
    else:
        return x-1
    

def solve(s):
    turnsl=[]
    l=[int (x) for x in s.split()]
    #print l
    if max(l)==1:
        return 1
    turnsl.append(max(l))
    for cut in range(3,max(l)+1):
        turns=0
        moreturns=0
        for x in l:
            div=1
            while x/div+x%div>=cut:
                turns+=1
                div+=1
            x=x/div+x%div
            if x>moreturns:
                moreturns=x
        

        #print cut,turns,moreturns
        turnsl.append(turns+moreturns)
    #print turnsl
    return min(turnsl)
