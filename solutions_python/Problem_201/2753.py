import sys


def cases():
	count = int(sys.stdin.readline())
	for i in range(count):
		line = sys.stdin.readline()
		(N, K) = line.strip().split(" ")

		yield (i + 1, int(N), int(K))

def bath(N, K):
	stalls = [[i, N - i - 1] for i in range(N)]

	# print stalls

	last = None
	for i in range(K):
		# print "===="
		# print stalls

		items = []
		for i, pair in enumerate(stalls):
			if not pair == True:
				items.append((i, max(pair[0], pair[1]), min(pair[0], pair[1])))

		# print items

		first = max(item[2] for item in items)
		result = filter(lambda item: item[2] == first, items)

		if len(result) != 1:

			second = max(item[1] for item in result)
			result = filter(lambda item: item[1] == second, result)

		(index, ma, mi) = result[0]

		right_shift = stalls[index][1] + 1
		for i in range(index - 1, -1, -1):
			if stalls[i] == True: break

			stalls[i][1] -= right_shift 

		left_shift = stalls[index][0] + 1
		for i in range(index + 1, len(stalls)):
			if stalls[i] == True: break

			stalls[i][0] -= left_shift 

		stalls[index] = True

		last = (ma, mi)



	return last

def L(stalls, start):
	count = 0
	for i in range(start - 1, -1, -1):
		if stalls[i]: break

		count += 1

	return count

def R(stalls, start):
	count = 0
	for i in range(start + 1, len(stalls)):
		if stalls[i]: break

		count += 1

	return count

for i, N, K in cases():
	(ma, mi) = bath(N, K)
	print "Case #%d: %d %d" % (i, ma, mi)
	# break