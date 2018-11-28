import sys

cases = int(raw_input())

def possible(P, time):
	for special in range(0, time):
		# possible in time using special special minutes?
		used = 0
		max_h = time - special
		for k in P:
			while k > max_h:
				used += 1
				k -= max_h
		if used <= special:
			return True
	return False

for current_case in range(1, cases+1):
	D = int(raw_input())
	P = [int(k) for k in raw_input().split()]
	
	low, high = 0, max(P)
	while low + 1 < high:
		mid = (low+high)/2
		if possible(P, mid):
			high = mid
		else:
			low = mid
	
	print "Case #%d: %d" % (current_case, high)