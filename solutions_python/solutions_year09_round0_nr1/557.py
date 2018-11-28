import re

def f(x):
	return re.match(pat, x)
	
fp = open('A-large.in')
fo = open('A-large.out', 'w')
ips = fp.readline().split(' ')
L = int(ips[0])
D = int(ips[1])
N = int(ips[2])
dict = []
for i in range(0, D):
	dict.append(fp.readline().strip())

for j in range(0, N):
	pat = fp.readline().strip()
	pat = pat.replace('(', '[')
	pat = pat.replace(')', ']')
	res = filter(f, dict)
	#print ('Case #' + str(j+1) + ': ' + str(len(res)))
	fo.write('Case #' + str(j+1) + ': ' + str(len(res)) + '\n')
fo.close()
fp.close()
	
	
