import math

T = int(raw_input())

def area(R):
	return math.pi * R * R

def surface_area(R, H):
	return math.pi * 2 * R * H

def total_area(R, H):
	return area(R) + surface_area(R, H)

for i in xrange(T):
	radius_list = []
	height_list = []

	N, K = [int(s) for s in raw_input().split(" ")]
	for j in xrange(N):
		R, H = [int(s) for s in raw_input().split(" ")]
		radius_list.append(R)
		height_list.append(H)

	# find K largests surface_area
	picked_list = []
	picked_r = []
	picked_h = []

	for j in xrange(K):
		max_area = 0
		max_idx = -1

		for k in xrange(N - j):
			a = surface_area(radius_list[k], height_list[k])
			if a > max_area:
				max_area = a
				max_idx = k

		picked_h.append(height_list[max_idx])
		picked_r.append(radius_list[max_idx])
		picked_list.append(max_idx)
		del radius_list[max_idx]
		del height_list[max_idx]

	# find largest area among K
	max_area = 0
	max_idx = -1
	max_total_area = 0
	for j in xrange(K):
		a = area(picked_r[j])

		if a > max_area:
			max_area = a
			max_idx = j

	max_total_area = total_area(picked_r[max_idx], picked_h[max_idx])

	m2_area = 0
	m2_idx = -1
	for j in xrange(N - K):
		a = total_area(radius_list[j], height_list[j])
		if a > max_total_area:
			max_total_area = a
			m2_idx = j

	if m2_idx != -1:
		min_sur = surface_area(picked_r[max_idx], picked_h[max_idx])
		min_idx = max_idx
		for j in xrange(K):
			if j == max_idx:
				continue

			a = surface_area(picked_r[j], picked_h[j])
			if a < min_sur:
				min_sur = a
				min_idx = j

		del picked_list[min_idx]
		del picked_h[min_idx]
		del picked_r[min_idx]
	else:
		del picked_list[max_idx]
		del picked_h[max_idx]
		del picked_r[max_idx]

	ans = max_total_area
	for j in xrange(K - 1):
		ans += surface_area(picked_r[j], picked_h[j])

	print "Case #%d: %.9f" % ((i + 1), ans)
