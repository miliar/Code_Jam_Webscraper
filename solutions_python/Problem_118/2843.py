from math import sqrt
n = int(input())
def is_num(a):
    return a - int(a)
for i in range(n):
    a,b = map(int,input().split())
    ans = 0
    for j in range(a,b+1):
        if list(str(j)) == list(str(j))[::-1] and is_num(sqrt(j)) == 0:
            if list(str(int(sqrt(j)))) == list(str(int(sqrt(j))))[::-1]:
                ans+=1
    print('Case #',i+1,':',ans,sep = '')