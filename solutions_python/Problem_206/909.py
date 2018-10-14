import sys

inp_name = sys.argv[1]
out_name = sys.argv[2]

def max_speed(ki,si,d):
	t = float(d - ki)/si
	s = float(d)/t
	return s

def get_max_speed(k,d):
	max_s = max_speed(k[0][0],k[0][1],d)
	for i in k:
		b = max_speed(i[0],i[1],d)
		max_s = min(max_s,b)
	return max_s

def print_result(a):
	g = open(out_name,'w')
	for i in xrange(len(a)):
		g.write('Case #'+str(i+1)+': '+a[i]+'\n')
	g.close()

def parse():
	f = open(inp_name)
	t = int(f.readline())
	ans = []
	for i1 in xrange(t):
		d_n = f.readline().strip().split(' ')
		d = float(d_n[0])
		n = int(d_n[1])
		k_s = []
		for i2 in xrange(n):
			k_s1 = f.readline().strip().split(' ')
			k_s1 = [float(j1) for j1 in k_s1]
			k_s.append(k_s1)
		ans.append(str(get_max_speed(k_s,d)))
	f.close()
	print_result(ans)

parse()
