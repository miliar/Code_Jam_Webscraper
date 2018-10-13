fin = open('input.in', 'r')
lines = iter(fin.readlines())
fin.close()
lines.next()

fout = open('out.txt', 'w+')

def flip(cake, k):
	blah = {'+': '-', '-': '+'}
	for i in range(k):
		cake[i] = blah[cake[i]]
	return cake

for num, line in enumerate(lines):
	cake, k = line.split()
	k = int(k)
	cake = list(cake)
	count = 0
	for i in range(len(cake)):
		c = cake[i]
		if c == '-' and k+i <= len(cake):
			cake = cake[:i] + flip(cake[i:], k)
			count += 1
	if all(a is '+' for a in cake):
		fout.write('Case #%s: %s\n' %(str(num+1), count))
	else:
		fout.write('Case #%s: IMPOSSIBLE\n' %str(num+1))

fout.close()