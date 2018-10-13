fin = open('input.in', 'r')
lines = iter(fin.readlines())
fin.close()
lines.next()

def val(n):
	n = list(n)
	return n == sorted(n)


fout = open('out.txt', 'w+')

for num, line in enumerate(lines):
	n = map(int, list(line.split()[0]))
	while not val(n):
		for i in range(1,len(n)):
			prev = n[i-1]
			curr = n[i]
			if curr < prev:
				n[i-1] = (n[i-1] + 9) % 10
				n = n[:i] + [9 for _ in range(len(n[i:]))]
	fout.write('Case #%s: %s\n' %(str(num+1), str(int(''.join(map(str, n))))))

fout.close()