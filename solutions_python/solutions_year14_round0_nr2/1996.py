# Google Code Jam - 2014 Qualification Round B (Cookie Clicker Alpha)
# Kye W. Shi

in_file = open('/home/kyeshi_0913/Downloads/B-large.in').read()
lines = in_file.split('\n')
t = int(lines[0])
del lines[0]

def calc(obj):
	c, f, x = obj
	lowest = x/2

	time = 0
	rate = 2
	while True:
		est = time + x/rate
		if est <= lowest:
			lowest = est
			time += c/rate
			rate += f
		else: break

	return lowest

out = []
for i in range(t):
	parse = [float(n) for n in lines[i].split(' ')]
	out.append('Case #%d: %r' % (i+1, calc(parse)))

open('/home/kyeshi_0913/Downloads/B-large.out', 'a').write('\n'.join(out))
