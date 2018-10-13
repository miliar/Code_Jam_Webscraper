
fp = open("b_in.in",'r')
fp_out = open('b_out.out','w')

num = int(fp.readline())

for i in range(num):
	st = fp.readline().strip()
	t=len(st)
	num = [int(d) for d in st]
	#print num
	check = 1
	for j in range(t-1):
		if num[j] >num [j+1] and j+1 <t and  check:
			#print '*'
			num[j] = num[j]-1
			for k in range(j+1,t):
				num[k] = 9
			
		elif num[j] == num[j+1] and check:
			#print '**'
			index = j
			for	k in range(j,t-1):
				if num[k] > num[k+1]:
					index = k
					num[j] = num[j]-1
					for m in range(j+1,t):
						num[m] = 9
					break

		
	ans = 0		
	for x in range(len(num)):
		ans += num[x]*pow(10,t-1-x)
	fp_out.write('Case #')
	fp_out.write(str(i+1))
	fp_out.write(": ")
	fp_out.write(str(ans))
	fp_out.write('\n')

fp.close()
fp_out.close()

