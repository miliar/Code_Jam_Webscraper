lines = open('C-large-1.in').read().split('\n')

T = int(lines[0])
lines = lines[1:]

def palindrom(n):
	return str(n)==''.join(list(reversed(str(n))))

a = []
for i in range(1,10**7+1):
	if palindrom(i) and palindrom(i**2):
		a.append(i**2)


f2 = open('3.out', 'w')

for t in range(T):
	s = 'Case #'+str(t+1)+': '
	x,y = [int(x) for x in lines[t].split()]
	s+= str(len([z for z in a if z>=x and z<=y]))
	f2.write(s+'\n')