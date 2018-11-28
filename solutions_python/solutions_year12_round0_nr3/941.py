fi=open('C-small-attempt0.in','r')
fo=open('new.txt','w')

def cycle(i):
    return i[-1]+i[:-1]

t=int(fi.readline())

for i in range(t):
    a,b=map(int,fi.readline().split())
    nums=[True for j in range(b+1)]
    count=0
    for n in range(a,b+1):
        nums[n]=False
        t=str(n)
        prev=[]
        for c in range(len(str(n))):
            t=cycle(t)
            if int(t) >= a and int(t) <= b and nums[int(t)] and t not in prev:
                count+=1
            prev.append(t)
    fo.write('Case #%d: %d\n'%(i+1,count))
fo.close()
            
        
