f = open('pan.in', 'r+')
open('pan.txt', 'w').close()
n = open('pan.txt', 'r+')
l =  int(f.readline())
import sys
sys.setrecursionlimit(1500)
cases=[]
pans=[]
def switch(case, pan,n ):
    case = list(case)
    if '-' in case:
        i = case.index('-')
        if i<=len(case)-pan:
            for l in range(pan):
                if case[i+l]=='+':
                    case[i+l]='-'
                elif case[i+l]=='-':
                    case[i+l]='+'
            return switch("".join(case),pan, n+1)
        return -199
    else:
        return n
        
        


for line in f:
    cases.append(line.split(" ")[0])
    pans.append(int(line.split(" ")[1]))
    
print(l, cases, sep="   ")
for c in range(len(cases)):
    print(c)
    case=cases[c]
    if '+' not in case:
        if len(case)%pans[c]==0:
            n.write("Case #" + str(c+1)+": "+str(int(len(case)/pans[c]))+"\n")
        else:
            n.write("Case #" + str(c+1)+": IMPOSSIBLE"+"\n")
    elif '-' not in case:
            n.write("Case #" + str(c+1)+": 0"+"\n")
    else:
            out=switch(case,pans[c], 0)
            if out>-199:
                n.write("Case #" + str(c+1)+": "+str(out)+"\n")
            else:
                n.write("Case #" + str(c+1)+": IMPOSSIBLE"+"\n")
                
         




    
n.close()
f.close()
