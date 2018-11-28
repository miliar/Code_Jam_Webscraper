#2012 codejam problem 1

def getit(alist):
    res =0
    s = int(alist[1])
    p = int(alist[2])
    for key in alist[3:]:
        if (int(key) == 3*p-3 or int(key)== 3*p-4) and s>0 and int(key)>p:
            res +=1
            s -=1
        elif int(key) >= 3*p-2:
            res +=1
    return res
    


in1 = open(r'c:\users\douglas\documents\home\yiqiang\2012codejam\B-small-attempt0.in')
out1 = open(r'c:\users\douglas\documents\home\yiqiang\2012codejam\bsmallout.txt', 'w')
lines = in1.readline()
n = int(lines.rstrip())
m=1
result=[]
lines =in1.readline()
while lines !='':
    temp = lines.rstrip().split()
    res = getit(temp)
    result.append(res)    
    lines =in1.readline()

for key in result:
    out1.write("Case #"+str(m)+': '+str(key)+'\n')
    m+=1
in1.close()
out1.close()
