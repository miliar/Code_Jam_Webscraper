import math


f = open('A-large.in', 'r')

for idx , line in enumerate(f):
        if idx>0:
        
            n = int(line.partition(' ')[0])
            k = int(line.partition(' ')[2])
            
            okres = pow(2,n) 

            if k < okres-1:
	           print 'Case #' + str(idx) + ': OFF'
            else:


	        	state = k - (okres-1)
		        state = float(state)/okres

		        if math.modf(state)[0] ==0:
		        	print 'Case #' + str(idx) + ': ON'
		        else:
		        	print 'Case #' + str(idx) + ': OFF'
        
