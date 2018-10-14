import sys

def solve(N):
	d = map(int, str(N))
	k = len(d)

	i = 0
	while i < k and d[i] == 1:
		if i < k-1 and d[i+1] == 0:
			return '9'*(k-1)
		i += 1

	start_of_this_grp = i 
	while i < k:
		if i < k-1 and d[i+1] > d[i]:
			start_of_this_grp = i+1
		if i < k-1 and d[i+1] < d[i]:
			d[start_of_this_grp] = d[start_of_this_grp] - 1
			d = d[:start_of_this_grp+1] + [9]*(k-start_of_this_grp-1)
		i += 1

	return int(''.join(map(str, d)))

 #    7581
 #    6999

 #    7813
 #    7799

 #    1034
 #    999

 #    1103
 #    999

	# 1*2*3*4*5*6*7*8*9*

lines = sys.stdin.readlines()

T = int(lines[0].strip())

for t in range(T):
	N = int(lines[t+1].strip())
	answer = solve(N)
	print "Case #{}: {}".format(t+1, answer)
