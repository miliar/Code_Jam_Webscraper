f = open('A-large.in', 'r')
o = open('output.txt', 'w')

N = int(f.readline().strip())

for i in range(N):
	s = f.readline().strip().split(' ')
	mx = int(s[0])
	l = map(int,list(s[1]))

	sum = 0
	counter = 0
	for j in range(mx+1):
		if sum+counter >= j:
			sum = sum + l[j]
		elif l[j] == 0:
			sum = sum + l[j]
		elif sum+counter < j:
			counter =  j-sum
			sum = sum + l[j]

	o.write('Case #{}: {}\n'.format(i+1, counter))

f.close()
o.close()