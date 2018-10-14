#tidy number
def isTidy(n): #string
	for i in range(len(n)-1):
		if int(n[i])>int(n[i+1]):
			return i
	return -1

fi = open('input.in','r')
out = open('out.out','w')
out.write("")
out.close()
out = open('out.out','a')
N = int(fi.readline())
for i in range(N):
	out.write("Case #%d: " %(i+1))
	n = fi.readline()[:-1]
	p = isTidy(n)
	while p!=-1:
		m = list(n)
		m[p] = str(int(m[p])-1)
		for k in range(p+1,len(m)):
			m[k] = '9'
		n = ''.join(e for e in m)
		p = isTidy(n)
	out.write("%d\n"%(int(n)))	
fi.close()
out.close()

