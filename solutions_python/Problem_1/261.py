import sys
import copy

N = int( sys.stdin.readline() )
for n in range(N):
	S = int( sys.stdin.readline() )
	searchers = {}
	for s in range(S):
		line = sys.stdin.readline()
		searchers[line] = s
	Q = int( sys.stdin.readline() )
	prev_vals = [0] * S
	curr_vals = [0]
	for q in range(Q):
		line = sys.stdin.readline()
		query_num = searchers[line]
		curr_vals = []
		for s in range(S):
			if s == query_num: val = 999999
			else: val = min( prev_vals[s],  min(prev_vals) + 1 )
			curr_vals.append(val)
		prev_vals = curr_vals
	print "Case #" + str(n+1) + ":", min(curr_vals)
	#print searchers
	#print curr_vals
	#print
