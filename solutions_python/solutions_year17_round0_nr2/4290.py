T = input()




def solvesolve():

    nstr = str(N)
    nlist = map(int,list(nstr))

    if nlist[0] == 1:
        if 0 in nlist:
            return "9" * (len(nlist) - 1)
    
    
    if True:
        while True:
            lp = -1
            vcnt = 0
            rev_nlist = nlist[::-1]
            for i in range(len(nlist)-1,0,-1):
                vcnt += 1
                if nlist[i-1] > nlist[i]:
                    lp = i-1
                    break

            if lp == -1:
                return nstr
            
            rig = str(nlist[i-1]-1) + ("9" * vcnt)
            lef = nstr[:lp]

            nstr = lef + rig
            nlist = map(int,list(nstr))

    



def solve():

    ans = solvesolve()           
    print "Case #%d: %s"%(t,ans)
            
            



for t in range(1,T+1):
    N = input()
    solve()

