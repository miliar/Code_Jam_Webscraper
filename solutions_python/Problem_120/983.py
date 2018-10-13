import math

f = open('bull_eyes_input_small', 'r')

n = int(f.readline().strip())

def count_small_gap(r, t):
	white_r = r
	paint_left = t
	r_count = 0
	while paint_left > 0:
		black_r = white_r + 1
		paint_amount = black_r + white_r
		if paint_left < paint_amount:
			break
		r_count += 1
		paint_left -= paint_amount
		white_r = black_r + 1
	return r_count

def count_big_gap(r, t):
	max_c = (t * 0.5) ** 0.5
	#print max_c
	r_count = max_c
	while True:
		p = (r * 2 + 2 * r_count - 1) * r_count
	#	print p
		if p <= t:
			break
		else:
			r_count -= 1
	return r_count


for i in range(n):
	(r, t) = [int(j) for j in f.readline().strip().split()]

	if (t / r) > 100000:
		r_count = count_big_gap(r, t)
	else:
		r_count = count_small_gap(r, t)

	print "Case #%d: %d" % (i + 1, r_count)







