q={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q',' ':' '}

def decode(s):
	d=""
	for i in s:
		d=d+q[i]
	return d

fp=open("A-small-attempt0.in")
n=fp.readline().strip()
i=1
while True:
	n=fp.readline().strip()
	if n=='':
		break
	x=decode(n)
	print "Case #"+str(i)+":",x
	i=i+1

