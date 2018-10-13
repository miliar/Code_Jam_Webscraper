def isTidy(n):
	n = list(map(int, str(n)))
	for i in range(0,len(n)-1):
		if n[len(n)-1-i] < n[len(n)-2-i]:
			return False
	return True

def lastTidy(n):
	if isTidy(n):
		return n
	else:
		n = list(map(int, str(n)))
		for i in range(0,len(n)-1):
			if n[len(n)-1-i] < n[len(n)-2-i]:
				n[len(n)-2-i] = n[len(n)-2-i] - 1
				n = n[:len(n)-1-i]
				new = ['9'] * (i + 1)
				n.extend(new)
		n = int(''.join(map(str,n)))
		return lastTidy(n)
			
#print lastTidy(916623890580249613)

results=[]
with open('B-large.in') as inputfile:
    for line in inputfile:
    	results.append(line.strip().split(','))

out = open("foo.txt", 'wb')
for i in range(1, int(results[0][0])+1):
	out.write('Case #%s: %s \n' % (i, lastTidy(int(results[i][0]))))