def solve( x ):
    n = int(input())
    l =[]
    for i in range(0,4):
        t = input()
        if ( i == n-1 ):
            l = list(map(int,t.split()))
    m = int(input())
    k = []
    for i in range(0,4):
        t = input()
        if ( i == m-1 ):
            k = list(map(int,t.split()))
    mark = 0
    ans = -1
    for  i in l:
        if ( i in k ):
            mark += 1
            ans = i
    if ( mark == 1 ):
        print("Case #%d: %d"%(x,ans))
    elif ( mark >= 2 ):
        print("Case #%d: Bad magician!"%x)
    else:
        print("Case #%d: Volunteer cheated!"%x)

t = int(input())
for i in range(1,t+1):
    solve(i)
