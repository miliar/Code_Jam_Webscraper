#!/usr/bin/env python
import sys

def main():
	def my_min(a, b):
		if a is None: return b
		if b is None: return a
		return min(a, b)

	def my_sum(a, b):
		if None in (a, b): return None
		return a + b

	n_cases = int(raw_input())
	for case in range(n_cases):
		M, V = map(int, raw_input().split(' '))
		nodes = [None]
		for i in range((M-1)/2):
			G, C = map(int, raw_input().split(' '))
			nodes.append((G, C))
		for i in range((M+1)/2):
			if int(raw_input()):
				nodes.append((None, 0))
			else:
				nodes.append((0, None))

		for i in range((M-1)/2, 0, -1):
			#print i
			G, C = nodes[i]

			get = [0,0]

			left = nodes[2*i]
			right = nodes[2*i+1]

			if G == 1:	# AND
				get[0] = my_min(left[0], right[0])
				get[1] = my_sum(left[1], right[1])
			else:		# OR
				get[0] = my_sum(left[0], right[0])
				get[1] = my_min(left[1], right[1])

			if C:
				changed = [0,0]
				if G == 0:	# Was AND
					changed[0] = my_min(left[0], right[0])
					changed[1] = my_sum(left[1], right[1])
				else:		# Was OR
					changed[0] = my_sum(left[0], right[0])
					changed[1] = my_min(left[1], right[1])
				for x in [0,1]:
					if changed[x] is not None:
						get[x] = my_min(get[x], 1 + changed[x])

			nodes[i] = get
			#print "Node #%d: %s" % (i, get)

		ans = nodes[1][V]
		if ans is None:
			ans = "IMPOSSIBLE"
		print "Case #%d: %s" % (case + 1, ans)
main()
