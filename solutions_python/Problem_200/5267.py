import math
#t=int(input())
c="B-small-attempt8"#input()
fname="C:\Users\Sidhant\Downloads\\"+str(c)+".in"
s=[]

def tidy(a):
    l=len(a)
    if l == 1:
        return 1
    elif a[0]<=a[1]:
        return tidy(str(long(long(a)%math.pow(10,(l-1)))))
    else:
        return 0
"""  
for e in range(t):
    x=str(input())
    s.append(x)
"""
with open(fname,'r') as f:
    s = f.readlines()
s = [x.strip() for x in s]
#"""
i=1
for each in s:
    for n in range(long(each),0,-1):        
        if tidy(str(n)):
            with open("sub8.out",'a+') as o:
            #print(("Case #{}: {}".format(i, n)))#
                o.write("Case #{}: {}\n".format(i, n))
            i+=1
            break
