# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(raw_input())):
    n=int(raw_input())
    arr=[[0 for k in range(n)] for j in range(n)]
    for j in range(n):
        u,v=map(int,raw_input().split())
        arr[u][v]=1
        arr[v][u]=1
    g,k=map(int,raw_input().split())
    l=[0 for j in range(g)]
    r=[0 for j in range(g)]
    for j in range(g):
        u,v=map(int,raw_input().split())
        l[j]=u
        r[j]=v
    for j in range(1,n+1):
        for val in l:
            if arr[]
        
