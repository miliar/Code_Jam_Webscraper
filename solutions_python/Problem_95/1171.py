f = open('A-small-attempt1.in.txt', 'r')
t = f.readline()
t = int(t)
g = open('A.out', 'w')

print t

decode = 'ynficwlbkuomxsevzpdrjgthaq '
decode = list(decode)
abc = 'abcdefghijklmnopqrstuvwxyz '
abc = list(abc)

x = 0
while (x < t):
	s = f.readline()
	s = list(s)
	s.pop()
	r = []
	for e in s:
		r.append(abc[decode.index(e)])
	r = ''.join(r)
	r = 'Case #' + str(x+1) + ': ' + r
	if (x != t-1):
		r = r + '\n'
	g.write(r)
	x = x + 1