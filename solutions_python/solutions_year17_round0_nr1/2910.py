
fp = open("a_in.in",'r')
fp_out = open('a_out.out','w')
test = int(fp.readline())

for z in range(test):
	raw = fp.readline().strip().split()

	st = [d for d in raw[0]]

	k = int(raw[1])

	cnt= 0
	ans = 0
	for x in st:
		if x == '-':
			cnt+=1
	#print cnt

	for i,x in enumerate(st):
		#print i
		if x=='-' and k+i-1 < len(st):
			ans+=1

			cnt-=1
			st[i]='+'
			for y in range(i+1,i+k):
				if st[y] == '+':
					st[y]='-'
					cnt+=1
				else:
					st[y] = '+'
					cnt-=1
	fp_out.write('Case #')
	fp_out.write(str(z+1))
	fp_out.write(": ")
	if cnt==0:
		fp_out.write(str(ans))
		fp_out.write('\n')
	else:
		fp_out.write('IMPOSSIBLE')
		fp_out.write('\n')

fp.close()
fp_out.close()