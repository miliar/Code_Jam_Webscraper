T = int(raw_input())

for j in range(T):
	N = int(raw_input())

	oa = map (lambda x : float(x), raw_input().split())
	ob = map (lambda x : float(x), raw_input().split())

	oa.sort()
	ob.sort()

	#print oa
	#print ob

	# Deceit
	a = oa[:]
	b = ob[:]

	de = 0
	while len(a) > 0:
		if a[0] < b[0]:
			a = a[1:]
			b = b[:-1]
		else:
			de += 1
			remover = 0
			while remover+1 < len(b) and a[0] > b[remover + 1]:
				remover = remover+1
			a = a[1:]
			b = b[:remover] + b[remover+1:]


	# Unfair
	a = oa[:]
	b = ob[:]

	fa = 0
	while len(a) != 0:
		playa = a[0]
		a = a[1:]

		playb = None
		for i in range(len(b)):
			if b[i] > playa:
				playb = b[i]
				b = b[:i] + b[i+1:]
				break

		if playb == None:
			playb = b[0]
			b = b[1:]

		if playa > playb:
			fa += 1

	print ("Case #%(id)s: %(de)s %(fa)s" % {"id" : j+1, "de" : de, "fa" : fa})
