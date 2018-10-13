cases = []
with open('A-large.in') as f:
    n = int(f.readline())
    for i,line in enumerate(f):
        if i%2 == 0:
            n = int(line)
        else:
            mush = [int(j) for j in line.split()]
            diff = []
            for a in range(0,n-1):
                diff.append(mush[a]-mush[a+1])
            x,y,prev,rate = 0,0,0,max(max(diff),0)
            for j,k in enumerate(diff):
                x += max(0,k)
                y += max(min(mush[j],rate),0)
                prev = k
            cases.append('Case #'+str(i//2+1)+': '+str(x)+' '+str(y)+'\n')

with open('A-large.out','w+') as g:
    g.writelines(cases)