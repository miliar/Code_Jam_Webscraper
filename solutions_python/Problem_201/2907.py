import sys

def largest_empty(arr):
	i = 0
	l = len(arr)
	e = l-1
	m = 0
	t = None
	while i < l-1:
		if arr[i] == 1:
			i+=1
			continue
		c = i
		while arr[c] == 0:
			c+=1
		nt = (i, c-1)
		if nt[1]-nt[0] > m:
			t = nt
			m = nt[1]-nt[0]
		i=c
	return nt

def empty_size(empty):
	return empty[1]-empty[0]-1

def break_largest_empty(empties):
	m = 0
	bigger = None
	for empty in empties:
		if empty[1] - empty[0] > m:
			m = empty[1] - empty[0]
			bigger = empty
	empties.remove(bigger)
	nl = (bigger[0], bigger[0] + int((bigger[1] - bigger[0])/2))
	nr = (bigger[0] + int((bigger[1] - bigger[0])/2), bigger[1])
	empties.append(nl)
	empties.append(nr)
	return empty_size(nl), empty_size(nr)

T = int(sys.stdin.readline().splitlines()[0])

for case in range(T):
	line = sys.stdin.readline().split()
	N = int(line[0])
	K = int(line[1])
	empties = [(0,N+1)]
	for j in range(K):
		ls, rs = break_largest_empty(empties)
		if j == K - 1:
			# print ('empties: ' + str(empties))
			print ('Case #' + str(case+1) + ': ' + str(max(ls, rs))) + ' ' + str(min(ls, rs))

