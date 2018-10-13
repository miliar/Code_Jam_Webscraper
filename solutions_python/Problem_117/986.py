#!/usr/bin/python

testcase=int(raw_input())

for testcasei in range(testcase):
    params=raw_input().split(" ")
    rown=int(params[0])
    coll=int(params[1])

    targetfields=[]
    workingfields=[]
    for r in range(rown):
        targetfields.append([int(x) for x in raw_input().split(" ")])
        workingfields.append([100 for x in range(coll)])

    def cuthorz():
        donesomething=False
        for r in range(rown):
            targetheight=max(targetfields[r])
            workingmaxheight=max(workingfields[r])
            if(workingmaxheight>targetheight):
                donesomething=True
                for c in range(coll):
                    if(workingfields[r][c]>targetheight):
                        workingfields[r][c]=targetheight
                    
        return donesomething

    def cutvert():
        donesomething=False
        for c in range(coll):
            thecol=[targetfields[x][c] for x in range(rown)]
            thewcol=[workingfields[x][c] for x in range(rown)]
            targetheight=max(thecol)
            workingmaxheight=max(thewcol)
            if(workingmaxheight>targetheight):
                donesomething=True
                for r in range(rown):
                    if(workingfields[r][c]>targetheight):
                        workingfields[r][c]=targetheight
                    
        return donesomething

    while(cuthorz() or cutvert()):
        pass
    
    notpos=False
    for r in range(rown):
        for c in range(coll):
            if(workingfields[r][c]!=targetfields[r][c]):
                notpos=True
                break
        if(notpos):
            break

    if(notpos):
        print("Case #%s: NO"%(testcasei+1))
    else:
        print("Case #%s: YES"%(testcasei+1))
