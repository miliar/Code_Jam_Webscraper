filename = 'BS0'
fin = open(filename+'.in', 'r')
fout = open(filename+'.out', 'w')


for x in range(int(fin.readline().strip())):
	tmp = fin.readline().strip().split(' ')
	N = [int(n) for n in tmp[0]]
	# print(tmp[0])

	#res = '' if len(N) > 1 else str(N[0])
	for i in range(len(N) - 1):
		n = N[i]
		n1 = N[i+1]
		if n > n1:
			N[i+1:] = [9]*(len(N)-i-1)
			chlast = (i==0)
			for j in range(i, 0, -1):
				if N[j]-1 >= N[j-1]:
					N[j] -= 1
				else:
					N[j] = 9
					if j <= 1:
						chlast = True
			if chlast:
				if N[0] == 1:
					N = N[1:]
				else:
					N[0] -= 1
			break

	res = ''.join([str(n) for n in N])
	strOut = 'Case #'+str(x+1)+': '+str(res)+'\n'
	fout.write(strOut)
	print(strOut)
		
fout.close()
fin.close()
