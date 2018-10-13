inp = open('input_A_large.txt','r')
T = int(inp.readline().strip())
f = open('results_A_large.txt','w')


for t in range(0,T):
	max, arr = inp.readline().strip().split()
	max = int(max)

	up = 0
	add = 0
	for k in range(0,max+1):
		if up >= k:
			up += int(arr[k])
		else:
			add += k - up
			up += k - up + int(arr[k])

	f.write('Case #'+str(t+1)+': '+str(add)+'\n')
	print add

inp.close()
f.close()
