import re

combinations = []
oppositions = []

def combine(a, b):
	for c in combinations:
		if c.combine(a,b):
			return True, c.output
	return False, '';

def has_opposition(elements):
	for op in oppositions:
		return op.has_opposition(elements)
	return False, -1

class Combination:
	def combine(self, a, b):
		if (self.inputs.__contains__('%s%s'%(a,b))):
			return True
		return False
	def __init__(self, comb):
		spl = re.findall('.', comb)
		self.output = spl.pop()
		self.inputs = []
		self.inputs.append('%s%s'%(spl[0],spl[1]))
		self.inputs.append('%s%s'%(spl[1],spl[0]))

	
	
class Opposition:
	def __init__(self, opp):
		self.components = []
		self.components = re.findall('.', opp)
	
	def has_opposition(self, elements):
		if not self.components.__contains__(elements[0]) : return False, -1
		if elements.__contains__(self.components[0]) and elements.__contains__(self.components[1]) : 
			index = ''
			if elements[0] == self.components[0]: index = elements.index(self.components[1])
			else : index = elements.index(self.components[0])
			flag_comb, sub = combine(elements[index-1], elements[index])
			if not flag_comb: 
				return True, index
			else: 
				elements.pop(index)
				elements[index-1] = sub
				return self.has_opposition(elements)
		return False, -1

x = file('input.txt')
f = open ('solution.txt', 'w')

n_tests = int(x.readline())
for i in range(0, n_tests) :
	combinations = []
	oppositions = []
	output = []
	to_consume = ''
	n_comb = 0
	case_spl = []
	
	case = x.readline()
	case_spl = case.split(' ')
	n_comb = int(case_spl.pop(0))
	for j in range(0, n_comb):
		c = Combination(case_spl.pop(0))
		combinations.append(c)
	n_opp = int(case_spl.pop(0))
	for j in range(0, n_opp):
		o = Opposition(case_spl.pop(0))
		oppositions.append(o)
	n_elements = int(case_spl.pop(0))
	to_consume = case_spl.pop();
	list_el = re.findall('.', to_consume)
	while list_el != []:
		if list_el.__len__() > 1:
			flag_comb, el = combine(list_el[0], list_el[1])
			if flag_comb:
				list_el.pop(0)
				list_el.pop(0) 
				output.append(el)
				continue
			flag_op, del_index = has_opposition(list_el)
			if flag_op:
				for d in range(0, del_index+1):
					list_el.pop(0)
				output = []
			else: output.append(list_el.pop(0))				
		else: output.append(list_el.pop(0))

	f.write("Case #%s: %s\n"%(int(i)+1, output))

f.close()
x = file('solution.txt')
x = x.read();
x = x.replace("'", '')
f = open('solution.txt', 'w') 
f.write(x)
f.close()
