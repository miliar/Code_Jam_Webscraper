import sys

inp_name = sys.argv[1]
out_name = sys.argv[2]

def possible_flip(st, k):
	i=0
	no_flips = 0
	s = [x for x in st]
	while(i<len(s)):
		if i==(len(s)-k):
			if s[i:]==['-']*k:
				return str(no_flips+1)
			elif (s[i:]==['+']*k):
				return str(no_flips)
			else:
				return 'IMPOSSIBLE'
		else:
			if s[i]!='+':
				no_flips+=1
				for j in xrange(i,i+k):
					if s[j]=='+':
						s[j] = '-'
					else:
						s[j] = '+'
		i+=1
	return str(no_flips)


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
		t = line.strip().split(' ')
		ans.append(possible_flip(t[0], int(t[1])))
	f.close()
	print_result(ans)

parse()
