import sys


def sample(d, r):
	if r > 0: return min(d+1, 30)
	return d

def sample_max(d, r):
	if r != 1: return min(sample(d,r)+1, 30)
	return sample(d,r)

def has_special(d, r):
	if (d == 0 and r < 2) or (d == 9 and r > 1) or d==10: return False
	return True

l = {}

def recurse(t_list, i, m, n, p):
	#print( "recurse %d %d %d %d" % (i, m, n, p) )
	if i >= len(t_list): return 0
	t = t_list[i]
	#print( "t %d" % (t))
	if l[t][0] >= p: 
		return 1 + max( recurse(t_list, i+1, True, n, p), recurse(t_list, i+1, False, n, p))
	elif len(l[t]) > 1 and l[t][1] > 0 and m and n > 0:
		if l[t][1] >= p:
			return 1 + max( recurse(t_list, i+1, True, n-1, p), recurse(t_list, i+1, False, n-1, p))
	return max( recurse(t_list, i+1, True, n, p), recurse(t_list, i+1, False, n, p))

x = sys.stdin.readline()
x = int(x)
i = 1
while i <= x:
	input = sys.stdin.readline()
	input = input.split()
	N = int(input[0])
	S = int(input[1])
	p = int(input[2])

	j = 1
	t_list = []
	temp_s = ""
	while j <= N:
		t = int(input[2+j])
		if l.has_key(t) == False:
			d = t / 3
			r = t % 3
			if has_special(d,r): 
				l[t] = (sample(d,r), sample_max(d,r))
			else:
				l[t] = (sample(d,r), -1)
		t_list.append(t)
		temp_s +=str(l[t]) + ", "
		j += 1

	#print N, S, p, t_list, temp_s

	# do stuff
	out = max( recurse(t_list, 0, True, S, p), recurse(t_list, 0, True, S, p) )
	print("Case #%d: %s" % (i, out)) 
	i += 1

#print l
