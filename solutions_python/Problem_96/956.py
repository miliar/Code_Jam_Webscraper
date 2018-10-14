fi=open('B-large.in','r')
fo=open('tout.txt','w')

t=int(fi.readline())

for i in range(t):
    nums = map(int,fi.readline().split())
    n,s,p=nums[:3]
    nums = nums[3:]
    count=0
    for j in nums:
        if j >= 3*p - 2:
            count += 1
        elif j >= 3*p-4 and s > 0 and j>=p:
            s-=1
            count += 1
    fo.write('Case #%d: %d\n'%(i+1,count))
            
fo.close()
fi.close()
