t = int(input())
for testcase in range(1, t + 1):
	line = input().split(" ")
	N = int(line[0])
	R = int(line[1])
	O = int(line[2])
	Y = int(line[3])
	G = int(line[4])
	B = int(line[5])
	V = int(line[6])

	ring = ['_' for i in range(N)]
	valid = True
	#only R Y B matters
	if R >= Y and R >= B:
		ring[0] = 'R'
		R -= 1
	elif Y >= R and Y >= B:
		ring[0] = 'Y'
		Y -= 1
	else:
		ring[0] = 'B'
		B -= 1
	if ring[0] == 'B':
		for i in range(1, N):
			# no adjacent R AND (Y and B both unavailable OR Y is available but R >= Y OR B is available but R >= B)
			if (R > 0 and ring[(i - 1)%N] != 'R' and ring[(i + 1)%N] != 'R') and (((ring[(i - 1)%N] == 'Y' or ring[(i + 1)%N] == 'Y') and (ring[(i - 1)%N] == 'B' or ring[(i + 1)%N] == 'B')) or (ring[(i - 1)%N] != 'Y' and ring[(i + 1)%N] != 'Y' and R >= Y) or (ring[(i - 1)%N] != 'B' and ring[(i + 1)%N] != 'B' and R >= B)):
				ring[i] = 'R'
				R -= 1
			elif (B > 0 and ring[(i - 1)%N] != 'B' and ring[(i + 1)%N] != 'B') and (((ring[(i - 1)%N] == 'Y' or ring[(i + 1)%N] == 'Y') and (ring[(i - 1)%N] == 'R' or ring[(i + 1)%N] == 'R')) or (ring[(i - 1)%N] != 'Y' and ring[(i + 1)%N] != 'Y' and B >= Y) or (ring[(i - 1)%N] != 'R' and ring[(i + 1)%N] != 'R' and B >= R)):
				ring[i] = 'B'
				B -= 1
			elif (Y > 0 and ring[(i - 1)%N] != 'Y' and ring[(i + 1)%N] != 'Y') and (((ring[(i - 1)%N] == 'R' or ring[(i + 1)%N] == 'R') and (ring[(i - 1)%N] == 'B' or ring[(i + 1)%N] == 'B')) or (ring[(i - 1)%N] != 'R' and ring[(i + 1)%N] != 'R' and Y >= R) or (ring[(i - 1)%N] != 'B' and ring[(i + 1)%N] != 'B' and Y >= B)):
				ring[i] = 'Y'
				Y -= 1
			else:
				valid = False
				break
	else:
		for i in range(1, N):
			# no adjacent R AND (Y and B both unavailable OR Y is available but R >= Y OR B is available but R >= B)
			if (R > 0 and ring[(i - 1)%N] != 'R' and ring[(i + 1)%N] != 'R') and (((ring[(i - 1)%N] == 'Y' or ring[(i + 1)%N] == 'Y') and (ring[(i - 1)%N] == 'B' or ring[(i + 1)%N] == 'B')) or (ring[(i - 1)%N] != 'Y' and ring[(i + 1)%N] != 'Y' and R >= Y) or (ring[(i - 1)%N] != 'B' and ring[(i + 1)%N] != 'B' and R >= B)):
				ring[i] = 'R'
				R -= 1
			elif (Y > 0 and ring[(i - 1)%N] != 'Y' and ring[(i + 1)%N] != 'Y') and (((ring[(i - 1)%N] == 'R' or ring[(i + 1)%N] == 'R') and (ring[(i - 1)%N] == 'B' or ring[(i + 1)%N] == 'B')) or (ring[(i - 1)%N] != 'R' and ring[(i + 1)%N] != 'R' and Y >= R) or (ring[(i - 1)%N] != 'B' and ring[(i + 1)%N] != 'B' and Y >= B)):
				ring[i] = 'Y'
				Y -= 1
			elif (B > 0 and ring[(i - 1)%N] != 'B' and ring[(i + 1)%N] != 'B') and (((ring[(i - 1)%N] == 'Y' or ring[(i + 1)%N] == 'Y') and (ring[(i - 1)%N] == 'R' or ring[(i + 1)%N] == 'R')) or (ring[(i - 1)%N] != 'Y' and ring[(i + 1)%N] != 'Y' and B >= Y) or (ring[(i - 1)%N] != 'R' and ring[(i + 1)%N] != 'R' and B >= R)):
				ring[i] = 'B'
				B -= 1
			else:
				valid = False
				break

	#print (ring)

	if valid:
		print("Case #{}: {}".format(testcase, ''.join(ring)))
	else:
		print("Case #{}: IMPOSSIBLE".format(testcase))
