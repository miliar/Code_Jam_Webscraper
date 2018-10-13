import sys 

def war(N, naomi, ken):
	naomi.sort()
	ken.sort()

	i = 0
	j = 0
	s = 0
	m = []

	while (i < N and j < N):
		if naomi[i] < ken[j]:
			s -= 1
			i += 1
		else: 
			s += 1
			j += 1
		m.append(s)

	while i < N:
		s -= 1
		i += 1
		m.append(s)

	while j < N:
		s += 1
		j += 1
		m.append(s)
	
	return [N + min(m), max(m)]

T = int(sys.stdin.readline())

for tc in range(T):
	N = int(sys.stdin.readline())
	naomi = map(float, (sys.stdin.readline()).split())
	ken = map(float, (sys.stdin.readline()).split())

	output = war(N, naomi, ken)
	print "Case #" + str(tc + 1) + ": " + str(output[0]) + " " + str(output[1]) 