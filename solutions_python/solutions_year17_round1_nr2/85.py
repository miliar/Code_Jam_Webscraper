t = int(raw_input())  # read a line with a single integer

def ceildiv(a, b):
    return -(-a // b)

for numtest in xrange(1, t + 1):
    n,p=[int(k) for k in raw_input().split(" ")]
    r=[int(k) for k in raw_input().split(" ")]
    q=[[0]*p for j in range(n)]
    for i in range(n):
        q[i]=[int(k) for k in raw_input().split(" ")]
    qr={}
    qrs={}
    for i in range(n):
        qr[i]=[(max(1,ceildiv((q[i][j]*10),11*r[i])),(q[i][j]*10)/(9*r[i]),q[i][j]) for j in range(p)]
        qrs[i]=sorted(qr[i])
  #  print q
 #   print qr
  #  print qrs
    recurs=[0]*n
    res=0
    while max(recurs)<p:
        #vire too small
        for i in range(n):
            if recurs[i]<p:
                kk=[qrs[k][recurs[k]][0] for k in range(n) if recurs[k]<p and k!=i]
                try:
                    maxmin=max(kk)
                except:
                    maxmin=0
                while recurs[i]<p and (qrs[i][recurs[i]][0]>qrs[i][recurs[i]][1] or qrs[i][recurs[i]][1]<maxmin):
        #            print "elimination de {} du {}".format(i,qrs[i][recurs[i]][2])
                    recurs[i]+=1
        #now i guess everyone has the maxmin in it
        if max(recurs)<p:
            mymax=max([qrs[k][recurs[k]][0] for k in range(n)])  
            mymin=min([qrs[k][recurs[k]][1] for k in range(n)])  
            if mymax<=mymin:
                res+=1
                tp=""
                for i in range(n):
                    tp+="{},".format(qrs[i][recurs[i]][2])
                    recurs[i]+=1
            #    print tp
       

    print "Case #{}: {}".format(numtest,res)
   # if numtest==1:
    #    1/0