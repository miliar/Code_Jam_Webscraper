import sys
myStr = sys.stdin.read()
myWords = myStr.split()

caseN = 0
for p in range (1,int(myWords[0])*2,2):
    len = myWords[p]
    abantu = myWords[p+1]
    caseN += 1
    
    c = 0
    f = 0
    ctr= 0
    for x in abantu:
        c = c + int(x)
        ctr+=1

        if(c < ctr):
            f = f + 1
            c = c+1
    print("Case #{}: {}".format(caseN,f))    
