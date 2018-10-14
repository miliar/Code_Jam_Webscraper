import inspect
base = inspect.getfile(inspect.currentframe())[:-3]
data = file(base+'.in', 'r')
out = file(base+'.out', 'wb')

T = int(data.readline())
for case in range(1,T+1):
	v = data.readline().split()
	N = int(v[0])
	ops = []
	for i in range(1,1+2*N,2):
		ops.append((v[i],int(v[i+1])))
	print ops
	pos = {'O':1, 'B':1}
	freetime = {'O':0, 'B':0}
	other = {'O':'B', 'B':'O'}
	total = 0
	for robot, button in ops:
		# minimum turn is 1 second (already in position)
		turn = max(1, 1 + abs(pos[robot]-button) - freetime[robot])
		pos[robot] = button
		freetime[robot] = 0
		freetime[other[robot]] += turn
		total += turn
		#print total, turn, pos, freetime
	print total
	out.write("Case #{0}: {1}\n".format(case, total))
