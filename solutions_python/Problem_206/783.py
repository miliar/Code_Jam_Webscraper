fin = open('input.in', 'r')
lines = iter(fin.readlines())
fin.close()
lines.next()
fout = open('out.txt', 'w+')

for num, line in enumerate(lines):
	d, n = map(int, line.split())

	horses = []
	for i in range(n):
		line = lines.next()
		k, s = map(int, line.split())
		time = float(d - k)
		time = time / s
		horses.append(time)

	max_t = max(horses)
	speed = d / max_t
	fout.write('Case #%s: %s\n' %(str(num+1), str(speed)))

fout.close()