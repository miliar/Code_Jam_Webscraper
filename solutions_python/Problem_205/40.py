#!/usr/bin/python

import sys
import collections

if len(sys.argv) != 2:
	print "usage: %s <input_file_name>" % sys.argv[0]
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def bfs(Hd, Ad, Hk, Ak, B, D):
	q = collections.deque()
	existed = set()
	existed.add((Hd, Ad, Hk, Ak))
	q.append((Hd, Ad, Hk, Ak, 1))
	while q:
		Hdc, Adc, Hkc, Akc, num_turn = q.popleft()
		if Hkc <= Adc:
			return str(num_turn)
		if Hdc > Akc:
			if (Hdc - Akc, Adc, Hkc - Adc, Akc) not in existed:
				q.append((Hdc - Akc, Adc, Hkc - Adc, Akc, num_turn + 1))
				existed.add((Hdc - Akc, Adc, Hkc - Adc, Akc))
			if B > 0 and (Hdc - Akc, Adc + B, Hkc, Akc) not in existed:
				q.append((Hdc - Akc, Adc + B, Hkc, Akc, num_turn + 1))
				existed.add((Hdc - Akc, Adc + B, Hkc, Akc))
			if Akc > 0 and D > 0 and (Hdc - max(0, Akc - D), Adc, Hkc, max(0, Akc - D)) not in existed:
				q.append((Hdc - max(0, Akc - D), Adc, Hkc, max(0, Akc - D), num_turn + 1))
				existed.add((Hdc - max(0, Akc - D), Adc, Hkc, max(0, Akc - D)))
		else:
			if D > 0 and Hdc > max(0, Akc - D) and (Hdc - max(0, Akc - D), Adc, Hkc, max(0, Akc - D)) not in existed:
				q.append((Hdc - max(0, Akc - D), Adc, Hkc, max(0, Akc - D), num_turn + 1))
				existed.add((Hdc - max(0, Akc - D), Adc, Hkc, max(0, Akc - D)))
			if (Hd - Akc, Adc, Hkc, Akc) not in existed:
				q.append((Hd - Akc, Adc, Hkc, Akc, num_turn + 1))
				existed.add((Hd - Akc, Adc, Hkc, Akc))
	return 'IMPOSSIBLE'

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline().strip('\n')
		Hd, Ad, Hk, Ak, B, D = [int(x) for x in line.split(' ')]
		ret = bfs(Hd, Ad, Hk, Ak, B, D)
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
