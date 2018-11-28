input = open ('alien.txt', 'r')
output = open ('alienans.txt', 'w')

c = input.readline()
c = c.split()

Dic = ['' for i in xrange (int(c[1]))]
for i in xrange(int(c[1])):
	Dic[i] = input.readline()

for i in xrange( int(c[2])):
	que = ['' for j in xrange(int(c[0]))]
	d = input.readline()	
	if d[-1] != '\n':
		d += '\n'
	j = 0
	k = 0
	while j < len(d) - 1:
		if d[j] == '(':
			j += 1
			while d[j] != ')':
				que[k] += d[j]
				j += 1
			j += 1
			k += 1
		else:
			que[k] = d[j]
			k += 1
			j += 1
	ans = 0
	for k in Dic:
		for j in xrange(len(k) - 1):
			if k[j] not in que[j]:
				break
			if j == len(k) - 2:
				ans += 1
	output.write('Case #' + str(i + 1) + ': ' + str(ans) + '\n')
		

input.close()
output.close()

			