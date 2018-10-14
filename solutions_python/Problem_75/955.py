class elist:
    def __init__(self):
        self.l = []
        self.add_rule = {}
        self.rem_rule = {}

    def rule_comb(self, a, b, c):
        try: self.add_rule[a] += [(b, c)]
        except: self.add_rule[a] = [(b, c)]

        try: self.add_rule[b] += [(a, c)]
        except: self.add_rule[b] = [(a, c)]

    def rule_expl(self, a, b):
        try: self.rem_rule[a] += [b]
        except: self.rem_rule[a] = [b]

        try: self.rem_rule[b] += [a]
        except: self.rem_rule[b] = [a]

    def add(self, a):
		if self.l:
			last = self.l[-1]
			ok = 0
			try:
				for i in self.add_rule[a]:
					if last == i[0]:
						ok = 1
						self.l.pop(-1)
						self.l += [i[1]]
						break
			except:
				pass
			try:
				if ok == 0:
					for i in self.rem_rule[a]:
						if i in self.l:
							self.l = []
							ok = 2
							break
			except:
				pass
			if ok == 0:
				self.l += [a]
		else:
			self.l = [a]

cases = input()
for i in range(cases):
	line = raw_input().split(' ')
	n = int(line.pop(0))

	e = elist()
	for j in range(n):
		a, b, c = line.pop(0)
		e.rule_comb(a, b, c)
	
	n = int(line.pop(0))
	for j in range(n):
		a, b = line.pop(0)
		e.rule_expl(a, b)
	
	n = int(line.pop(0))
	for j in line[0]:
		e.add(j)

	print "Case #%d: %s"%(i+1, '[' + ', '.join(e.l) + ']')

