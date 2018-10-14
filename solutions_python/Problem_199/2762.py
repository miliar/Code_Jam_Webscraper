import sys
sys.stdout=open("output.txt","w")
for index in range(int(raw_input())):
    arr=map(str,raw_input().split())
    s=arr[0]
    k=(int)(arr[1])
    n=len(s)
    cnt=0
    stringarr=[0 for l in range(n)]
    for j in range(n):
        if s[j]=='+':
            stringarr[j]=1
        else:
            stringarr[j]=0
    #print strarr
    for j in range(n):
        if stringarr[j]==0 and n-j>=k:
            cnt+=1
            for m in range(j,j+k):
                stringarr[m]=1-stringarr[m]

    #print strarr
    if stringarr.count(1)==n:
        print 'Case #'+str(index+1)+': '+str(cnt)
    else:
        print 'Case #'+str(index+1)+': '+"IMPOSSIBLE"
sys.stdout.close()