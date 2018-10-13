def cal(data,T):
    s = 0;
    init =  data[0]
    for x in range(1,len(data)):
    	if data[x] <init:
    		s+= init -data[x] 
    		init = data[x]
    	else:
    		init = data[x]
    return s
def cal2(data,T):
    s = 0
    rate = 0
    for x in range(len(data)-1):
    	rate = max(rate,data[x]-data[x+1])
    
    for x in range(len(data)-1):
        if data[x] > rate:
            s += rate
        else:
            s+=data[x]
			
			
    return s
for tc in range(input()):
    T= map(int, raw_input().split())
    data = map(int,raw_input().split())      
    print "Case #%d: %d %d" % (tc+1,cal(data,T),cal2(data,T))
