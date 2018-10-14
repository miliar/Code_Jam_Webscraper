import re

def check(ind,nums):
    a=str(nums[ind])
    c=0
    for i in range(1,len(a)):
        a1=a[i:]+a[:i]
        if int(a1) in nums[ind+1:]:
            c+=1
    return c

text=open('C:\\Users\\Anshul\\Downloads\\C-small-attempt2.in','r')
N=int(text.readline())
for j in range(N):
    line=text.readline()
    ns=re.findall('\d+',line)
    count=0
    nums=list(range(int(ns[0]),int(ns[1])+1))
    for i in range(len(nums)):
        if check(i,nums)>0:
            count+=check(i,nums)
    f=open('C:\\Users\\Anshul\\Downloads\\out5.txt','a')
    f.write('Case #'+str(j+1)+': '+str(count)+'\n')
f.close()
#'Case #'+str(j+1)+': '+str(count)+'\n'
