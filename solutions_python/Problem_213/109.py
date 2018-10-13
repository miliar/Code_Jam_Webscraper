T = int(input())

for casenum in range(1, T+1):
	N, C, M = tuple([int(x) for x in input().split()])

	tickets = [[0]*N for x in range(C)]
	lens = [0]*C

	for i in range(M):
		P, B = tuple(int(x) for x in input().split())
		tickets[B-1][P-1] += 1
		lens[B-1] += 1

	rides = 0
	bumps = 0

	if C == 2:
		rides = max(lens[0], lens[1])
		biggest = 0
		if lens[1] > lens[0]:
			biggest = 1
		other = 1-biggest

		for i in range(N):
			diff = tickets[other][i] - (lens[biggest] - tickets[biggest][i])
			if diff > 0:
				if i == 0:
					rides += diff
				else:
					bumps += diff

	print("Case #", casenum, ": ", rides, " ", bumps, sep = "")