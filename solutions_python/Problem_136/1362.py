filestr = 'B-large'
# filestr = 'B-verysmall'
fin = open(filestr+'.in','r')
fout = open(filestr+'.out','w')

lines = fin.read().splitlines()
N = int(lines[0])
for i in range(N):
	a = lines[i+1].split(' ')
	c = float(a[0])
	f = float(a[1])
	x = float(a[2])
	if x>c:
		T = x
		newT = x/2
		dt = [c/2]
		j=0
		while T-newT>0:
			j = j+1
			T = newT
			newT = sum(dt)+x/(2+j*f)
			dt.append(c/(2+j*f))
	else:
		T=x/2

	str=  'Case #%d: %.7f\n'%(i+1,T)
	fout.write(str)
	# print str

fin.close()
fout.close()

