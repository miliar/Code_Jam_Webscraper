def main():
	n = int(input())
	for i in range(1, n+1):
		print("Case #%d: " % i, end="")
		solve()

def solve():
	ajat = [[], []]

	a, b = map(int, input().split())
	intervals = []
	for i in range(a):
		x, y = map(int, input().split())
		intervals.append((x, y, 0))
	for i in range(b):
		x, y = map(int, input().split())
		intervals.append((x, y, 1))

	intervals.sort(key=lambda x: x[0])

	shift = 0
	allocated = [0, 0]
	exchanges = 0

	x, y, kuka = intervals[0]
	allocated[kuka] += y - x
	prev = kuka
	prevend = y

	for i in intervals[1:]:
		x, y, kuka = i

		allocated[kuka] += y - x

		if prev == kuka:
			ajat[kuka].append(x - prevend)
		else:
			shift += y - x
			exchanges += 1
		
		prev = kuka
		prevend = y

	mn = 720*2 - intervals[-1][1] + intervals[0][0]
	if intervals[0][2] != intervals[-1][2]:
		shift += mn
		exchanges += 1
	else:
		ajat[intervals[0][2]].append(mn)

	if allocated[0] + sum(ajat[0]) > 720:
		extra = allocated[0] + sum(ajat[0]) - 720
		ajat[0].sort(key=lambda x: -x)
		s = 0
		while s < extra:
			s += ajat[0].pop(0)
			exchanges += 2
	elif allocated[1] + sum(ajat[1]) > 720:
		extra = allocated[1] + sum(ajat[1]) - 720
		ajat[1].sort(key=lambda x: -x)
		s = 0
		while s < extra:
			s += ajat[1].pop(0)
			exchanges += 2
	
	print(exchanges)

main()