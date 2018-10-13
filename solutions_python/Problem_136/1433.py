import time

start_time = time.time()

Output = []
T = int(raw_input())
for i in range(T):
	#print '==========='
	C,F,X = raw_input().split()
	C = float(C)
	F = float(F)
	X = float(X)
	
	cps = 2
	tottime = 0
	while X/cps > (X/(cps+F)+C/cps):
		tottime += C/cps
		cps += F
		#print cps
		
	tottime += X/cps

	Output += ["%.07f" % tottime]

		
for i in range(len(Output)):
	print 'Case #%d: %s' % (i+1, Output[i])
	
end_time = time.time()
#print end_time-start_time