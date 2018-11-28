from math import floor
def solve(x,n):
    alist = [x]
    for i in range(0,n-1):
        maxel = max(alist)-1
        if maxel%2==0:
            alist.append(maxel/2)
            alist.append(maxel/2)
            alist.remove(maxel+1)
        else:
            alist.append(floor(float(maxel)/2))
            alist.append(floor(float(maxel)/2)+1)
            alist.remove(maxel+1)
        #print(alist)
    truemax = max(alist)-1
    #print(truemax)
    if truemax%2==0:
        return (truemax/2,truemax/2)
    else:
        return (floor(float(truemax)/2)+1,floor(float(truemax)/2))
file = open("C-small-1-attempt0.in","r")
cnt = 0
for line in file:
    if cnt==0:
        cnt+=1
    else:
        red = line.strip().split(' ')
        print("Case #"+str(cnt)+": " + str(int(solve(int(red[0]),int(red[1]))[0]))+ ' '+str(int(solve(int(red[0]),int(red[1]))[1])))
        cnt+=1
