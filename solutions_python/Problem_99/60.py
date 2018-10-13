


def solve(a,b,prob):
	mini = b+2
	correct = 1
	correct_p = []
	for j in range(a):
		correct = correct*prob[j]
		correct_p.append(correct)

	for i in range(a+1):
		correct = 1
#		for j in range(a-i):
#			correct  = correct*prob[j]
		correct = correct_p[a-i-1]
		expt = correct*(b-a+1+2*i) + (1-correct)*(b-a+1+2*i+b+1)
		
		if expt<mini: mini=expt
#		print 'back for '
	return mini




if __name__=='__main__':



	f=open('A-large.in','r')
	fout = open('A.out','w')

	T = int(f.readline())

	for i in range(T):
		fout.write('Case #%d: '%(i+1))
		line = f.readline()
		a = int(line.strip().split()[0])
		b = int(line.strip().split()[1])

		line = f.readline()
		prob = [float(item) for item in line.strip().split()]
		
		ans = solve(a,b,prob)
		fout.write('%.6f\n'%ans)	


	f.close()
	fout.close()
