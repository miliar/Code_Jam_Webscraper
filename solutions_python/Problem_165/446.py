def loop(R,C,P):
	return ((C-1)/P+P)*R
		
			
			
		
for tc in range(input()):
    R,C,P = map(int,raw_input().split())
    print "Case #%d: %d" % (tc+1,loop(R,C,P))        
        
