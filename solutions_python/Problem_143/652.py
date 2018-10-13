def nlg():
	f_input = open('B-small-attempt0.in','r')
	f_output = open('B-small-attempt0.ou','w')
	case = int(f_input.readline().strip('\n'))
	for i in range(1,case+1):
		A,B,K = [int(j) for j in f_input.readline().strip('\n').split(' ')]
		combo = []
		for j in range(A):
			for k in range(B):
				if (j&k) < K:
					combo.append([j,k])
		f_output.write('Case #'+str(i)+': '+str(len(combo))+'\n')

	f_input.close()
	f_output.close()

if __name__ == '__main__':
	nlg()
