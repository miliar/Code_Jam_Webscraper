T = input()
for t in range(T):
	N, K = map(int, raw_input().split())
	set_of_free_stalls = [N]
	for k in range(K-1):
		n = (set_of_free_stalls.pop() - 1)
		L = n/2
		R = n/2 + n%2
		set_of_free_stalls.append(L)
		set_of_free_stalls.append(R)
		set_of_free_stalls.sort()
	n = set_of_free_stalls.pop() - 1
	print "Case #"+str(t+1)+': '+str(n/2 + n%2)+' '+str(n/2)

