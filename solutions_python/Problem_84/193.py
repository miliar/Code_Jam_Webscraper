# Problem A

def calc(p):
	used_list = []
	for i in range(len(p[0])-1):
		# Go through each column looking for 2x2 blocks
		for j in range(len(p)-1):
			if p[j][i] == "#" and p[j][i+1] == "#" and 	p[j+1][i] == "#" and p[j+1][i+1] == "#":
				# good 4x4 block then
				if (j, i) not in used_list and (j, i+1) not in used_list and (j+1, i) not in used_list and (j+1, i+1) not in used_list:
					p[j][i] = "/"
					p[j][i+1] = "\\"
					p[j+1][i] = "\\"
					p[j+1][i+1] = "/"
					used_list.append((j, i))
					used_list.append((j+1, i))
					used_list.append((j+1, i+1))
					used_list.append((j, i+1))
	for _i in range(len(p)):
		for _j in range(len(p[0])):
			if p[_i][_j] == "#":
				return False, p
	return True, p
	
# sample data
#s = [list(".##.."), list(".####"), list(".####"), list(".##..")]

f = open("A.in")
t = int(f.readline())
for _t in range(t):
	p = []
	r, c = map(int, f.readline().split())
	for _r in range(r):
		p.append(list(f.readline()[:-1]))
	print "Case #{0}:".format(_t+1)
	c = calc(p)
	if not c[0]:
		print "Impossible"
	else:
		for l in c[1]:
			print "".join(l)
f.close()
