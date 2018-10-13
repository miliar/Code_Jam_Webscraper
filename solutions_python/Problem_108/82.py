f = open("in1","r")
t = int(f.readline())

global d,l

for tt in range(1,t+1):
    n = int(f.readline())
    l = list()
    l.append([0,0])
    for i in range(n):
        l.append(map(int,f.readline().split()))
    l.append([int(f.readline()), 999999999999])
    result = "YES"
    d=[i for i in range(len(l))]
    d[1] = 0
    for j in range(1,len(l)-1):
        if d[j] == -1:
            result = "NO"
            break
        i = d[j]
#        print i,j,l[i],l[j]
        k = min(l[j][0]-l[i][0], l[j][1])
        for jj in range(j+1,len(l)):
            if l[j][0]+k < l[jj][0]:
                break
            ii = d[jj]
            if min(l[jj][0]-l[j][0], l[jj][1]) > min(l[jj][0]-l[ii][0], l[jj][1]):
                d[jj] = j
    if d[len(l)-1] == len(l)-1:
        result = "NO"
#    print l,d
    print "Case #{0}: {1}".format(tt, result)
