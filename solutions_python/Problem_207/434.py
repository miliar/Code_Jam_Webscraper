T = int(input())
for j in xrange(T):
    N,R,O,Y,G,B,V = [int(i) for i in str(raw_input()).split()]
    lis=[[R,"R"],[Y,"Y"],[B,"B"]]
    lis=sorted(lis, key = lambda col: col[0])
    if lis[0][0]+lis[1][0] <lis[2][0]:
        ans="IMPOSSIBLE"
        print "Case #"+str(j+1)+": "+ans
        continue
    ans=""
    num1=lis[0][0]+lis[1][0]-lis[2][0]
    num2=lis[1][0]-num1
    num3=lis[2][0]-lis[1][0]
    rep1=lis[2][1]+lis[1][1]+lis[0][1]
    rep2=lis[2][1]+lis[1][1]
    rep3=lis[2][1]+lis[0][1]
    ans=rep1*num1+rep2*num2+rep3*num3
    print "Case #"+str(j+1)+": "+str(ans)
    
    
    
    

    
        
