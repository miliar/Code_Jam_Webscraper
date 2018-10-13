#!/usr/bin/python

f1 = open("B-large.in", "r")
f2 = open("B-large.out", "w")

lines = f1.read().split("\n")

lines = lines[1:-1]

case = 0

for line in lines:
	case = case + 1

	comb = [] #combinations
	oppo = [] #opposed
	res = []
	
	tokens = line.split(" ")
	#print tokens

	#lee combinaciones
	for i in range(1, int(tokens.pop(0))+1):
		comb.append(tokens.pop(0))
	#print comb

	#lee opuestos
	for i in range(1, int(tokens.pop(0))+1):
		oppo.append(tokens.pop(0))
	#print oppo

	#lee invocaciones (y trabaja)
	for i in range(1, int(tokens.pop(0))+1):
		e = tokens[0][i-1]
		#print "LETRA "+e
		res.append(e)

		if len(res) > 1:
			algo = False
			combina = True
			while combina and len(res) > 1:
				combina = False
				for c in comb:
					#print "for c:"+c+"."+res[-1]+" - "+e
					if len(res) > 1 and ( c[0] == res[-2] and c[1] == res[-1] ) or ( c[1] == res[-2] and c[0] == res[-1] ):
						res.pop(-1)
						res.pop(-1)
						res.append(c[2])
						#print c[2]
						combina = True
						algo = True
						break
			if (not algo) and len(res) > 1:
				for o in oppo:
					#print "for o:"+c+"."+res[-1]+" - "+e
					for j in res[:-1]:
						if len(res) > 1:
							if ( o[0] == j and o[1] == res[-1] ) or ( o[1] == j and o[0] == res[-1] ):
								res = []
								algo = True
	print "Case #"+str(case)+": "+str(res)
	#print "Case #"+str(case)+": "+str(res)+"\n"

	f2.write(("Case #"+str(case)+": "+str(res)+"\n").replace("'", ""))

f1.close()
f2.close()
