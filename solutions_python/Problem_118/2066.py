# 2013Q C

from math import sqrt, floor

def is_fair(i):
    n = len(i)
    for j in range(n//2+1):
        if i[j] != i[n-j-1]:
            return False
    return True

# obtain number of cases
T = int(input())

for a in range(T):
    AB=input()
    AB=AB.split(' ')
    A=int(AB[0])
    B=int(AB[1])

    count=0

    for i in range(A,B+1):
        if is_fair(str(i)):
            p=sqrt(i)
            q=floor(p)
            if p == q:
                if is_fair(str(q)):
                    count=count+1

            

    print('Case #'+str(a+1)+': '+str(count))
