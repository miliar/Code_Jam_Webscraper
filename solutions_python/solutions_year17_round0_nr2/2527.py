t=int(input())
for i in range(t):
    n=int(input())
    a=132
    while a==132:
        j=n
        lst=list(map(int, str(j)))
        j = []
        j=list(lst)
        lst.sort()
        if (j==lst):
            a=n
        else:
            n-=1
    x=str(i+1)
    y=str(a)
    print("Case #"+x+":",y)
