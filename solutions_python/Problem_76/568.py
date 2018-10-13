import sys
sys.stdin=open('C-large.in')
sys.stdout=open('cl.out','w')
for T in range(int(input())):
    l=int(input())
    l=input().split()
    s=0
    for i in range(len(l)):
        l[i]=int(l[i])
    for i in l:
        s^=i
    if s:
        print("Case #{}: {}".format(T+1, "NO"))
    else:
        print("Case #{}: {}".format(T+1, sum(l)-min(l)))

