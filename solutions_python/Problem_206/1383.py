import sys
sys.stdout=open("output.txt","w")
for tc in range(int(raw_input())):
    d,n=map(int,raw_input().split())
    arr=[0 for i in range(n)]
    for j in range(n):
        k,s=map(int,raw_input().split())
        arr[j]=(d-k)/(1.0*s)
    time=max(arr)
    print 'Case #'+str(tc+1)+": "+'%.6f' % (d/(1.0*time))
sys.stdout.close()