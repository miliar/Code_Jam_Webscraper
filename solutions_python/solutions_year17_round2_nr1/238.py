def p1(D,horses):


	
	times = [float(D-h[0])/h[1] for h in horses]
	tm = max(times)
	return D/tm

T = int(input())
for t in range(T):
	D, N = input().split()
	D,N = int(D), int(N)
	horses = []
	for i in range(N):
		ki, si = input().split()
		ki, si = int(ki), int(si)
		horses.append((ki,si))
	
	print("Case #%d: %f"%(t+1,p1(D,horses)))
