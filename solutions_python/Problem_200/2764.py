import sys

inp_name = sys.argv[1]
out_name = sys.argv[2]

def istidy(s):
	current = s[0]
	for w in s:
		if w<current:
			return False
		else:
			current = w
	return True

def tidy(s):
	if len(s)==1:
		return s
	elif istidy(s):
		return s
	else:
		t = s[:-1]
		t = int(t)-1
		t = str(t)
		temp = tidy(t)
		temp = temp + '9'
		temp = int(temp)
		temp = str(temp)
		return temp

def print_result(a):
	g = open(out_name,'w')
	for i in xrange(len(a)):
		g.write('Case #'+str(i+1)+': '+a[i]+'\n')
	g.close()

def parse():
	f = open(inp_name)
	f.readline()
	ans = []
	for line in f:
		t = line.strip()
		ans.append(tidy(t))
	f.close()
	print_result(ans)

parse()

