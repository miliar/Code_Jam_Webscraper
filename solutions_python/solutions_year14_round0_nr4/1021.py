from bisect import bisect_left
f=open('D-large.in')
g=open('Result.in','w')
T=int(f.readline())
#T=int(raw_input())
for i in range(T):
    N=int(f.readline())
    #N=int(raw_input())
    Naomi=sorted(map(float,f.readline().split()))
    Ken=sorted(map(float,f.readline().split()))
    #Naomi=sorted(map(float,raw_input().split()))
    #Ken=sorted(map(float,raw_input().split()))
    deceiving=N
    kensmaller=0
    for n in Naomi:
        if n<Ken[kensmaller]:
            deceiving-=1
        else:
            kensmaller+=1
    realscore=0
    for n in Naomi:
        p=bisect_left(Ken,n)
        if p!=len(Ken):
            del Ken[p]
        else:
            del Ken[0]
            realscore+=1
    #print deceiving
    #print realscore
    g.write('Case #'+str(i+1)+': '+str(deceiving)+' '+str(realscore)+'\n')
g.close()
f.close()
            
    
