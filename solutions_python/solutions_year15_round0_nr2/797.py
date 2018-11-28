T = int(raw_input())  
for t in xrange(T):
    N=int(raw_input())
    pancakes = map(int, raw_input().split(' '))
    #print pancakes    
    
    ans=max(pancakes)
    minutes=0
    scenario=pancakes.count(9)
    while sum(pancakes)>len(pancakes):
        minutes+=1
        pancakes.sort()
        max_pancakes=pancakes.pop()
        if scenario==1 and max_pancakes==9 and not (len(pancakes)>=2 and pancakes[-2]>4):
            #print "scenario1"
            pancakes+=[max_pancakes//3, max_pancakes-max_pancakes//3]
        else:
            #print "scenario0"
            pancakes+=[max_pancakes//2, max_pancakes-max_pancakes//2]
        
        ans=min(ans, max(pancakes)+minutes)
    
              
    print "Case #%d: %s" % (t+1, ans)
  