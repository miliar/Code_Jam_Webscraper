import sys

def paired(com, z, v):
	for x in com:
		if x[0] == z and x[1] == v:
			return x[2]
		if x[0] == v and x[1] == z:
			return x[2]
	return 0

def combine(inv, com, z, opp):
	if len(inv) > 0:
		v = inv[len(inv)-1]
		a = paired(com, z, v)
		if a == 0:
			inv = oppose(inv, z, opp)
			return inv
		else:
			del inv[len(inv)-1]
			inv.append(a)
			return inv
	else:
		return [z]

def oppose(inv, z, opp):
	if cleared(inv,z,opp):
		return []
	else:
		inv.append(z)
		return inv

def cleared(inv,z,opp):
	for x in opp:
		if x[0] == z :
			if contains(inv, x[1]) :
				return True
		if x[1] == z :
			if contains(inv, x[0]) :
				return True		
	return False

def contains(inv, x):
	for z in inv:
		if x == z:
			return True
	return False
	
data = sys.stdin.readlines()
del data[0]

g = 1;

for x in data:
	a = x.split(None)
	com = []
	opp = []

	i = 1
	b = int(a[0])+i
	while i < b:
		com.append(a[i])
		i = i+1

	c = int(a[i])+i+1
	i = i+1
	while i < c:
		opp.append(a[i])
		i = i+1
	
	invv = []
	for z in a[i+1]:
		invv = combine(invv,com,z,opp)

	print ("Case #",g,": [",sep = '',end="")
	if len(invv)>0:
		print(invv[0],end="")
		del(invv[0])
		for x in invv:
			print (", ",end="")
			print (x,end="")
	print ("]")
	g = g+1;
	
