from operator import itemgetter
import math

num_args = int(input())

for case_number in range(1, num_args+1):
	N, K = input().split()
	N, K = int(N), int(K)

	pancakes = []
	for i in range(N):
		R, H = input().split()
		R, H = int(R), int(H)
		pancakes +=[(R, H, 2*math.pi*R*H)]

	widest = max(pancakes, key=itemgetter(0))
	pancakes = list(reversed(sorted(pancakes, key=itemgetter(2))))

	used_pancakes1 = list(reversed(sorted(pancakes[:K], key=itemgetter(0))))

	pancakes.remove(widest)
	used_pancakes2 = [widest] + pancakes[:K-1]

	area1 = used_pancakes1[0][0]*used_pancakes1[0][0]*math.pi
	for p in used_pancakes1:
		area1 += p[2]

	area2 = used_pancakes2[0][0]*used_pancakes2[0][0]*math.pi
	for p in used_pancakes2:
		area2 += p[2]

	area_total = max([area1, area2])

	print("Case #" + str(case_number) + ": " + "%.9f" % area_total)


