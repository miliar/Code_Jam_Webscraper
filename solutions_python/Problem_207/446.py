# {R, O(RY), Y, G(YB), B, V(RB)}.

def val(i,l,r):
	if(i == -1):
		return l.index(max(l))
	if(i == 0):
		if(l[3] > 0):
			return 3
		if(l[2] == 0 and l[4] == 0):
			return -1
		if(l[2] == l[4]):
			if(l[1] == l[5]):
				if(r[0] == 4):
					return 4
				else:
					return 2
			if(l[5] > l[1]):
				return 2
			else:
				return 4	
		if(l[2] > l[4]):
			return 2
		else:
			return 4
	if(i == 2):
		if(l[5] > 0):
			return 5
		if(l[0] == 0 and l[4] == 0):
			return -1
		if(l[0] == l[4]):
			if(l[1] == l[3]):
				if(r[0] == 4):
					return 4
				else:
					return 0
			if(l[3] > l[1]):
				return 0
			else:
				return 4	
		if(l[0] > l[4]):
			return 0
		else:
			return 4
	if(i == 4):
		if(l[1] > 0):
			return 1
		if(l[2] == 0 and l[0] == 0):
			return -1
		if(l[2] == l[0]):
			if(l[5] == l[3]):
				if(r[0] == 2):
					return 2
				else:
					return 0
			if(l[5] > l[3]):
				return 2
			else:
				return 0	
		if(l[2] > l[0]):
			return 2
		else:
			return 0
	if(i == 1):
		if(l[4] > 0):
			return 4
	if(i == 3):
		if(l[0] > 0):
			return 0
	if(i == 5):
		if(l[2] > 0):
			return 2
	return -1

t = int(input())
for i in range(1, t + 1):
	l = [0,0,0,0,0,0]
	s = input().split(" ")
	n = int(s[0])
	r = [0]*n
	for j in range(6):
		l[j] = int(s[j+1])
	# print(l,r)
	f = -1
	for j in range(n):
		f = val(f,l,r)
		# print(f)
		if(f == -1):
			break
		l[f] -= 1
		r[j] = f
	if(f == -1):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	first = r[0]
	last = r[-1]
	if(first == last):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	if(first == 0 and (last == 1 or last == 5)):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	if(first == 2 and (last == 1 or last == 3)):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	if(first == 4 and (last == 3 or last == 5)):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	if(last == 0 and (first == 1 or first == 5)):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	if(last == 2 and (first == 1 or first == 3)):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	if(last == 4 and (first == 3 or first == 5)):
		print("Case #{}: IMPOSSIBLE".format(i,))
		continue
	print("Case #{}: ".format(i,), end='')
	for c in r:
		if(c == 0):
			print("R", end='')
		if(c == 1):
			print("O", end='')
		if(c == 2):
			print("Y", end='')
		if(c == 3):
			print("G", end='')
		if(c == 4):
			print("B", end='')
		if(c == 5):
			print("V", end='')
	print()

