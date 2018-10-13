T = int(raw_input())  
for t in xrange(T):
    X, R, C = map(int, raw_input().split(' '))
    
    ans="GABRIEL"
    
    if (R*C)%X>0:
        ans="RICHARD"
    
    max_dims=[X//2+1, -(-X//2)]
    if max(R, C)<max(max_dims) or min(R, C)<min(max_dims):
        ans="RICHARD"
        
    if X>3 and max(R, C)>=max(max_dims) and min(R, C)<=min(max_dims):
        ans="RICHARD"       
              
    print "Case #%d: %s" % (t+1, ans)
  