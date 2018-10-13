# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def check(arr,j,n,k):
    queue=deque([])
    queue.append(j)
    a=[0 for i in range(n)]
    a[j]=-1
    cnt=0
    while len(queue)>0:
        j=int(queue.popleft())
        #print j
        for i in range(n):
            if a[i]!=-1 and arr[j][i]==5:
                cnt+=1
                a[i]=-1
                queue.append(i)
            if a[i]!=-1 and arr[j][i]==1:
                queue.append(i)
                a[i]=-1
            if cnt>=k:
                return True
for tc in range(int(raw_input())):
    n=int(raw_input())
    arr=[[0 for k in range(n)] for j in range(n)]
    for j in range(n-1):
        u,v=map(int,raw_input().split())
        arr[u-1][v-1]=1
        arr[v-1][u-1]=1
    g,k=map(int,raw_input().split())
    for j in range(g):
        u,v=map(int,raw_input().split())
        #print u,v
        arr[u-1][v-1]=5
    cnt=0
    #print arr
    for j in range(0,n):
        if check(arr,j,n,k):
            cnt+=1
    if cnt==0:
        print 0,"/",1
    else:
        gc=gcd(cnt,n)
        print cnt/gc,"/",n/gc
        
