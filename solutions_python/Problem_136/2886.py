import sys
import numpy as np
with open(sys.argv[1]) as f:
	content = f.readlines()
testcases = int(content[0].replace('\n',''))
print testcases
counter = 1
f=open('outfile','w')
for i in range(testcases):
	test = content[counter].replace('\n','').split(' ')
	C,F,X = [float(s) for s in test]
	cr = 2.0000000
	timeConsumedSoFar = 0
	while(1):
		prev = timeConsumedSoFar + X/cr		
		timeConsumed = C/cr
		cr = cr + F	
		next = timeConsumedSoFar + timeConsumed + X/cr
		if next < prev:
			timeConsumedSoFar = timeConsumedSoFar + timeConsumed 
			continue
		else:
			f.write('Case #'+str(i+1)+': %0.7f\n'% prev )
			break
	counter = counter + 1
	
