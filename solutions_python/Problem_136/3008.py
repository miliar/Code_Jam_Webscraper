#!/usr/bin/env python
import sys


def t_iter (X, F, f_cur):
	'''time to reach X with f_cur farms, each producing F'''
	return 1.0*X / (1.0*f_cur*F + 2.0)



def solve (num):
	(C, F, X) = map (float, sys.stdin.readline().split())
	t = 0.0
	f_cur = 0

	while (True):
		t_wait = t_iter (X, F, f_cur)    # time to reach X (wait)
		t_farm = t_iter (C, F, f_cur)	 # time to get next farm
		t_more_farm = t_farm + t_iter (X, F, f_cur+1)   # ... + reach X with one more farm
		#print ("current time: %f, farms: %d. t_wait: %f, t_farm: %f, t_more_farm: %f" % (t, f_cur, t_wait, t_farm, t_more_farm))
		#print ("current time: %f, farms: %d. t_wait: %f, t_farm: %f" % (t, f_cur, t_wait, t_farm), file=sys.stderr)
		if t_wait <= t_more_farm:
			t += t_wait
			break
		else:
			t += t_farm
			f_cur += 1

	print ("Case #%d: %.7f" % (num, t))




num_cases = int (sys.stdin.readline())

for case in range (1, num_cases+1):
	solve (case)


