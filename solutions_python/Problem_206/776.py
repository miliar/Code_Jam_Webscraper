import codejam as gcj

T = gcj.read_input('i')
for t in range(T):
	D, N, horses = gcj.read_input('i i->', 'i i')
	
	time_to_D = [float(D - K) / S for K, S in horses]
	
	print 'Case #%i:' % (t + 1), D / max(time_to_D)
