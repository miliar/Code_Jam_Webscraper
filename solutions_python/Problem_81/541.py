import sys, itertools

def calc_wp(i, n, s):
	won = 0.0
	tot = 0.0
	for j in range(0, n):
		p = (i,j)
		if p in s:
			won += s[p]
			tot += 1
	return won/tot
	
def calc_owp(i, n, s):
	tot = 0.0
	num_ops = 0
	for opp in range(0,n):
		if opp != i and (opp,i) in s:
			num_ops += 1
			#print opp, i, (opp,i) in s
			
			tmp = 0.0
			cnt = 0.0
			for (a,b) in s.keys():
				if a != i and b != i and (a == opp):
					#print a, b, s[(a,b)]
					tmp += s[(a,b)]
					cnt += 1
					#print a, b
			if cnt > 0:
				tot += tmp / cnt
		#won[opp] = tmp
	if num_ops > 0:
		return tot / num_ops
	else:
		return 0
	
def calc_oowp(i, n, s):
	res = 0.0
	tot = 0
	for j in range(0,n):
		if (i,j) in s:
			res += calc_owp(j, n, s)
			tot += 1
	if tot > 0:
		return res/tot
	
def calc_rpi(i, n, s):
	return 0.25 * calc_wp(i, n, s) + 0.50 * calc_owp(i, n, s) + 0.25 * calc_oowp(i,n,s)
		
filename = sys.argv[1]
f = open(filename)
o = open(filename + ".new.2.out", "wt")
num_tests = int(f.readline())
for t in range(0,num_tests):
	num_teams = int(f.readline())
	scores = {}
	for n in range(0,num_teams):
		xs = f.readline()
		for i in range(0, num_teams):
			x = xs[i]
			if x == '.':
				pass
			elif x == '0':
				scores[(n,i)] = 0
			else:
				scores[(n,i)] = 1
	#print scores
	#oowp = calc_oowp(0, num_teams, scores)
	#print oowp
	#print calc_owp(2, num_teams, scores)
	
	print "Case #%d:" % (t+1)
	for n in range(0, num_teams):
		#print n, calc_wp(n, num_teams, scores), calc_owp(n, num_teams, scores)

		print calc_rpi(n, num_teams, scores)
				
	
