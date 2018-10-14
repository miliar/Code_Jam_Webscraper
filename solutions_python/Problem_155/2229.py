f = open('A-large.in.txt','r')
t = open('results.txt','w')
cases = f.readline()
count = 0
import re

def do_it(line,l):
	b = re.split(' ',line)
	a = b[1][:-1]
	print a
	guys = []
	for i in range(len(a)):
		for j in range(int(a[i])):
			guys.append(int(i+1))
	invited,stand = 0,0
	while stand < len(guys):
		for i in range(len(guys)):
			if guys[i] <= len(guys[:i+1]):
				stand += 1
			else:
				stand = 0
				invited += 1
				guys.insert(i,i)
				break
	r = 'Case #'+str(count)+': '+str(invited)+'\n'
	print r
	return r

for line in f.readlines():
		print line
		count += 1
		t.write(do_it(line,len))

t.close()