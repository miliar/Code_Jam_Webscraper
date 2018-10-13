def getFriends(self):
    return self.friends


def getDetail(self):
    detail = []
    detail.append(self.name)
    detail.append(self.rollno)
    detail.append(self.gender)
    detail.append(self.email)
    detail.append(self.nativePlace)
    detail.append(self.friends)
    return detail

import sys
sys.stdout=open("output.txt","w")
tc=int(raw_input())


def getGender(self):
    return self.gender


def getEmail(self):
    return self.email


for i in range(tc):
    arr=map(str,raw_input().split())
    s=arr[0]
    k=(int)(arr[1])
    n=len(s)
    cnt=0
    strarr=[0 for l in range(n)]
    for j in range(n):
        if s[j]=='+':
            strarr[j]=1
        else:
            strarr[j]=0
    #print strarr
    for j in range(n):
        if strarr[j]==0 and n-j>=k:
            cnt+=1
            for m in range(j,j+k):
                strarr[m]=1-strarr[m]

    #print strarr
    if strarr.count(1)==n:
        print 'Case #'+str(i+1)+': '+str(cnt)
    else:
        print 'Case #'+str(i+1)+': '+"IMPOSSIBLE"
sys.stdout.close()