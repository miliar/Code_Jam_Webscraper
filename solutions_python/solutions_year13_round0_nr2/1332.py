f = open('large.in', 'r')
r = open('res.txt','w+')

n = int(f.readline())
res = ""

for i in range(0,n):
	dims = f.readline()
	dims_arr = dims.split(" ")
	N = int(dims_arr[0])
	M = int(dims_arr[1])
	
	a = []
	
	for n in range(0,N):
		l = f.readline()
		l_arr = l.split(" ")
		a += [[int(l_arr[j]) for j in range(0,M)]]
	
	max_line = [0 for n in range(0,N)]
	max_column = [0 for m in range(0,M)]
	
	for n in range(0,N):
		max_line[n] = max(a[n])
	for m in range(0,M):
		max_column[m] = max([a[j][m] for j in range(0,N)])

	feasible = True
	for n in range(0,N):
		for m in range(0,M):
			if (a[n][m] != min(max_line[n],max_column[m])):
				feasible = False
				
	if(feasible):
		res += "Case #"+str(i+1)+": YES\n"
	else:
		res += "Case #"+str(i+1)+": NO\n"
		
r.write(res)
r.close()