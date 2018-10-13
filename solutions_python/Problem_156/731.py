#!/usr/bin/python3
def minus(x):
	return max(0,x-1)

T = int(input())

for case in range(1, T+1):
	D = int(input())
	P = [int(x) for x in input().split(' ')]
	ref = [0]*D
	P.sort(reverse=True)
	last = P[0]
	ans = last

	pos = [P]

	i = 0

	while i<last:
		i+=1
		newPos = []
		newPos[:] = pos[:]
		for j in range(len(pos)):
			newPos[j] = list(map(minus, pos[j]))
			if newPos[j][0] == 0:
				ans = i
				break

			for k in range(1, pos[j][0]//2+1):
				tmp = pos[j][:]
				tmp.append(k)
				tmp[0]-=k
				tmp.sort(reverse=True)
				newPos.append(tmp)

		if ans != last:
			break
		pos[:] = newPos[:]

	print('Case #', case, ': ', ans, sep='')