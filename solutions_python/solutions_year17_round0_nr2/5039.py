import sys
def isTidyNumber(tidyNumber):
    temp=0
    for r in tidyNumber:
       if temp>int(r):
           return False
       else:
            temp=int(r)
            
    return True

arg=list(sys.argv)
fread = open(arg[1])
inputdata=fread.read().split("\n")
t=int(inputdata[0])

f =open(arg[2],"w")
count=0
for a in inputdata[1:]:
    count+=1
    data = a
    if len(data)==0:
        break
    if len(data)==1:
        f.write("Case #"+str(count)+": "+data+"\n")
    else:
        temp = int(data)
        for r in range(temp):
            if isTidyNumber(str(temp)):
                f.write("Case #"+str(count)+": "+str(temp)+"\n")
                break
            else:
                temp-=1
f.close