N = input()
class Node:
	def __init__(self):
		self.next = {}

test = 0
while N:
	test += 1
	N -= 1
	r = raw_input()
	dicte = Node()
	r = r.split()
	r[0] = int(r[0])
	r[1] = int(r[1])
	init = {}
	tot = 0
	for i in range(r[0]):
		directory = raw_input()
		directory = directory[1:]
		x = directory
		t = 0
		directory = []
		oi = ""
		for a in x:
			if (a == '/'):
				directory.append(oi)
				oi = ""
			else:
				oi = oi + a
		if (oi != ""):
			directory.append(oi)
		#print directory
		#del directory[0]

		while (directory[-1] == "" and len(directory) >= 1):
			del directory[-1]		
		#print directory
		past = dicte
		for aux in directory:
			if (past.next.has_key(aux) == False):
				past.next[aux] = Node()
			past = past.next[aux]



	for i in range(r[1]):
		directory = raw_input()
		#print directory	
		directory = directory[1:]
		x = directory
		t = 0
		directory = []
		oi = ""
		for a in x:
			if (a == '/'):
				directory.append(oi)
				oi = ""
			else:
				oi = oi + a
		if (oi != ""):
			directory.append(oi)
		#print directory
		#del directory[0]

		while (directory[-1] == "" and len(directory) >= 1):
			del directory[-1]		
		#print directory
		past = dicte
		for aux in directory:
			#print "Testando se %s existe" % (aux)
			#print  past.next
			if (past.next.has_key(aux) == False):
				past.next[aux] = Node()
				tot += 1
			past = past.next[aux]

	print "Case #%d: %d" % (test, tot)	
		
