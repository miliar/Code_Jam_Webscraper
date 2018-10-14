import math

ntc = int(input())

def circ_area(r):
	return math.pi*r*r

def side_area(r, h):
	return math.pi*(2*r) * h

for tc in range(ntc):
	n, k = map(int, input().split())

	rh_cakes = []
	hr_cakes = []
	for i in range(n):
		r, h = map(int, input().split())
		rh_cakes.append((r, h, i))
		hr_cakes.append((h, r, i))

	hr_cakes.sort(key=lambda item: side_area(item[1], item[0]))
	hr_cakes.reverse()

	max_surf = None
	for base_idx in range(n):
		r_base, h_base, id_base = rh_cakes[base_idx]
		cur_surf = circ_area(r_base) + side_area(r_base, h_base)

		stack_size = 1
		for i in range(n):
			if stack_size == k: break

			h_ot, r_ot, id_ot = hr_cakes[i]
			if id_ot == id_base: continue

			if r_ot <= r_base:
				cur_surf += side_area(r_ot, h_ot)
				stack_size += 1
				# print('v--selected: ({}, {}, #{})'.format(r_ot, h_ot, id_ot))

		# print('base=({}, {}), #{} cir={}'.format(r_base, h_base, id_base, cur_surf))
		if stack_size == k:
			if max_surf is None:
				max_surf = cur_surf
				# print('^WIN!')
			elif cur_surf > max_surf:
				max_surf = cur_surf
				# print('^WIN!')

	# print('n={}, k={}'.format(n, k))
	print("Case #{}: {:.9f}".format(tc+1, max_surf))
