 
 
 
def finishTime(f,d,s,D):
    if D == d:
        return 0
    f2 = (D-d)/(s*1.0)
    return max(f2,f)

 
p1 = open('file','r')
p = p1.read().split('\n')[1:-1]
i = 0
j = 1
o = open('out.txt','w')
while i < len(p):
    print "i is " + str(i)
    l = p[i]
    print "l in " + l
    l = l.split()
    D = int(l[0])
    N = int(l[1])
    H = map(lambda x: (int(x.split()[0]),int(x.split()[1])),p[i+1:i + N+1])
    print H
    print "d is:" + str(D)
    if D == H[0][0]:
        temp = 0
        print "1:" + str(temp)
    else:
        temp = (D - H[0][0])/(H[0][1]*1.0)
        print "2:" + str(temp)
    for k in range(1,N):
        temp = finishTime(temp,H[k][0],H[k][1],D)
        print "3:" + str(temp)
    r = D/(temp*1.0)
    i = i + 1 + N
    o.write('Case #' + str(j) + ': ' + str(r) + '\n')
    j += 1
    
    
p1.close()
o.flush()
o.close()
    
