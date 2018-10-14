for qq in xrange(1,int(raw_input())+1):
    c,f,x=[float(u) for u in raw_input().split()]

    #curr_cookies=0.0
    curr_rate=2.0
    curr_time=c/curr_rate
    ans = x/curr_rate
    curr_rate+=f

    #print x/curr_rate,curr_time,ans

    while( x/curr_rate + curr_time < ans):
        ans=x/curr_rate + curr_time
        curr_time+=c/curr_rate
        curr_rate+=f
          
    print 'Case #'+str(qq)+': '+str(ans)
    
        
