import sys
fopen=open('/Users/subodhyadav/Desktop/A-small-attempt0.in.txt','r')
fout=open('/Users/subodhyadav/Desktop/A-small-attempt0.out.txt','a')
for k in xrange(int(fopen.readline().strip())):
	x=int(fopen.readline().strip())
	l=[]
	for i in xrange(4):
		n=map(int,fopen.readline().strip().split())
		l.append(n)
	m=[]
	y=int(fopen.readline().strip())
	for i in xrange(4):
		n=map(int,fopen.readline().strip().split())
		m.append(n)
	c=0
	t=0
	for i in m[y-1]:
		if i in l[x-1]:
			c+=1
			t=i
	if c==1:
		fout.write("Case #")
		fout.write(str(k+1))
		fout.write(": ")
		fout.write(str(t))
		fout.write("\n")
	elif c==0:
		fout.write("Case #")
		fout.write(str(k+1))
		fout.write(": Volunteer cheated!\n")
	else:
		fout.write("Case #")
		fout.write(str(k+1))
		fout.write(": Bad magician!\n")
fout.close()
fopen.close()