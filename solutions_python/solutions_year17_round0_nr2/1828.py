import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def IsTidy(n):
    current = 0
    for x in str(n):
        if int(x) > current:
             current = int(x)
        elif int(x) < current:
            return False
    return True

def TidyNumber(n):
    finalnum = n
    current = 0
    for x in range(len(str(n))):
        if int(str(n)[x]) < current:
            finalnum = int(n) - int(str(n)[x:]) - 1
            break
        else:
            current = int(str(n)[x])
    return finalnum
    

inp = open("io.in","r")
out = open("ol.out","w")
cases = int(inp.readline())
for casenum in range(1,cases+1):
    case = int(inp.readline())
    answer = case
    tidynum = TidyNumber(answer)
    while not IsTidy(tidynum):
        tidynum = TidyNumber(tidynum)
    out.write("Case #{}: {}\n".format(casenum,tidynum))
    

inp.close()
out.close()
