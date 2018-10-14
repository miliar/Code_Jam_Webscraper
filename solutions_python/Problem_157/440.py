from collections import defaultdict
#wrong way round
grid = [('1','1','+1'),('1','i','+i'),('1','j','+j'),('1','k','+k'),
		('i','1','+i'),('i','i','-1'),('i','j','-k'),('i','k','+j'),
		('j','1','+j'),('j','i','+k'),('j','j','-1'),('j','k','-i'),
		('k','1','+k'),('k','i','-j'),('k','j','+i'),('k','k','-1')]
def q(a,b):
	flip = 0
	if a[0] == "-":
		flip = 1-flip
	if b[0] == "-":
		flip = 1-flip
	r = None
	for (ar,br,cr) in grid:
		if a[1]==br and b[1]==ar:
			r = cr
			break
	assert r != None
	if flip:
		if r[0] == '+':
			return '-'+r[1]
		if r[0] == '-':
			return '+'+r[1]
	else:
		return r

for x in ['+1','-1','-j','+j','-i','+i','-k','+k']:
	c = 1
	cur = x
	while cur != '+1':
		c += 1
		cur = q(cur,x)
	print (x,c)

with open('in.txt','rb') as fin, open('output33.txt','w') as fout:
	case = 1

	it = iter(fin.readlines())
	_ = next(it)

	for line in it:
		print ("\n\n\n")
		print ("case " + str(case))
		L,X = [int(c) for c in line.split()]
		line = next(it)
		xs = ["+" + c for c in list(line) if c == 'i' or c == 'j' or c == 'k']
		
		# #print (xs)
		# x = reduce(q,xs,'+1')

		# c = 1
		# cur = x
		# while cur != '+1':
		# 	c += 1
		# 	cur = q(cur,x)

		# #print (xs,x,c)

		# if X>2*c:
		# 	X=2*c

		cs = xs*X
		cs_val = reduce(q,cs,'+1')

		cum = []		
		cur = '+1'
		for c in cs:
			cum.append(cur)
			cur = q(cur,c)
		cum.append(cur)

		cum_bk = []		
		cur = '+1'
		for c in reversed(cs):
			cum_bk.append(cur)
			cur = q(c,cur)
		cum_bk.append(cur)
		cum_bk=list(reversed(cum_bk))

		#print ('for the string: ' + str(cs))
		#print (cum)
		#print(cum_bk)

		for i in range(L*X):
			assert(q(cum[i],cum_bk[i])==cs_val)

		front = [] # lengths
		back = []

		for length,c in enumerate(cum):
			if c == '+i':
				front.append(length)
		for length,c in enumerate(cum_bk):
			if c == '+k':
				back.append(length)
		#print ("front:" + str(front))
		#print ("bk:" + str(back))

		res='NO'
		for f in front:
			for b in back:
				if f<b:
					# find y s.t. cum[f] * y = cum[b]
					if q(cum[f],'+j') == cum[b]:
						res='YES'
						break

		fout.write("Case #" + str(case) + ": " + res + "\n")
		case += 1

