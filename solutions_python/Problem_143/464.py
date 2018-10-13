T = int(raw_input())

for _t in range(1,T+1):
	l = [int(x) for x in raw_input().split(' ')]

	a,b,k = l[0],l[1],l[2]

	answer = 0
	for i in range(a):
		for j in range(b):
			if i&j < k:
				answer += 1

	print "Case #{0}: {1}".format(_t,answer)