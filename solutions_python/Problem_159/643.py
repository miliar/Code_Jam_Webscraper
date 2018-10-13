
f =open('A-large.in','r')
fout = open('large_result.txt','w')

casenum = int(f.readline().split('\n')[0])
for case in range(casenum):
    num = int(f.readline().split('\n')[0])
    lst = f.readline().split('\n')[0].split(' ')
    mush = []
    for char in lst:
        mush.append(int(char))
    meth1 = 0
    meth2 = 0
    i = 1
    while(i<len(mush)):
        k = mush[i]- mush[i-1]
        if k <0:
            meth1 += abs(k)
        i += 1
    #method 2
    speed = []
    for j in range(len(mush)-1):
        speed.append(mush[j]-mush[j+1])
    maxs = max(speed)
    for m in range(len(mush)-1):
        if mush[m] >= maxs:
            meth2 += maxs
        else:
            meth2 += mush[m]

    
    
    fout.write('Case #'+str(case+1)+': '+str(meth1)+' '+str(meth2))
    fout.write('\n')
            
    
fout.close()
