T = int(raw_input())

for test_case in range(T):
	D, N = [int(x) for x in raw_input().split()]
	horses = [[int(x) for x in raw_input().split()] for _ in range(N)]
	arrival_time = [float(D - k)/s for [k,s] in horses]
	answer = float(D) / max(arrival_time)
	print "Case #%s: %.10f"%(test_case+1, answer)
