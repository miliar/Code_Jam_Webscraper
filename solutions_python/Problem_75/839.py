a = open('b.in').read().strip()
outp = open('b.out','wt')
b = a.split('\n')
case = int(b[0].strip())
def finder(ite, ls):
	for k in ls:
		if k[0] == ite:
			return True
	else:
		return False
def finder2(ite,ls):
	for k in ls:
		if k[0] == ite:
			return k
def combin(somels, comls):
	if len(somels) < 2:
		return somels
	else:
		if somels[-2] not in comls:
			return somels
		else:
			if finder(somels[-1], comls[somels[-2]]):
				s = finder2(somels[-1], comls[somels[-2]])
				p = somels[0:-2]
				p.append(s[1])
				return combin(p, comls)
			else:
				return somels
	return somels
def erase(somels, erals):
	if len(somels) < 2:
		return somels
	else:
		p = somels[-1]
		if p not in erals:
			return somels
		else:
			for k in somels[0:-1]:
				if finder(k, erals[p]):
					return []
			return somels
	return somels
def invoker(somestr):
	p = somestr.split(' ')
	combils = {}
	opposels = {}
	res = []
	combcase = int(p[0])
	for i in range(1,combcase+1):
		str1 = p[i]
		if str1[0] not in combils:
			combils[str1[0]] = [(str1[1],str1[2])]
		else:
			combils[str1[0]].append((str1[1],str1[2]))
		if str1[1] not in combils:
			combils[str1[1]] = [(str1[0],str1[2])]
		else:
			combils[str1[1]].append((str1[0],str1[2]))

	opposecase = int(p[combcase+1])
	for i in range(1,opposecase+1):
		str2 = p[combcase+1+i]
		thes = (str2[0], str2[1])
		if str2[0] not in opposels:
			opposels[str2[0]] = [(str2[1],1)]
		else:
			opposels[str2[0]].append((str2[1],1))
		if str2[1] not in opposels:
			opposels[str2[1]] = [(str2[0],1)]
		else:
			opposels[str2[1]].append((str2[0],1))
	cheol = p[-1]
	for i in range(len(cheol)):
		if i == 0:
			res.append(cheol[i])
		else:
			res.append(cheol[i])
			res = erase((combin(res,combils)),opposels)
	return res
def genstri(ls):
	if len(ls) == 0:
		return "[]"
	a = "["
	for k in range(len(ls)):
		if k == len(ls)-1:
			a = a+str(ls[k])+"]"
			return a
		else:
			a = a+str(ls[k])+", "

 	return a
for k in range(1,case+1):
	port = invoker(b[k])
	thestr = "Case #"+str(k)+": "+genstri(port)+"\n"
	outp.write(thestr)
outp.close()
