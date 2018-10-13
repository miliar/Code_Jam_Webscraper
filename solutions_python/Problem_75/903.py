#!/usr/bin/python

num_cases = int(raw_input())

for i in range(0, num_cases):
	parameters   = raw_input().split(' ')
	num_combines = int(parameters[0])
	if num_combines > 0:
		combines   = parameters[1:(1 + num_combines)]
		parameters = parameters[(1 + num_combines):]
	else:
		combines = []
		parameters = parameters[1:]
	num_opposed  = int(parameters[0])
	if num_opposed > 0:
		opposed = parameters[1:(1 + num_opposed)]
		parameters = parameters[(1 + num_opposed):]
	else:
		opposed = []
		parameters = parameters[1:]
	
	num_invokes  = int(parameters[0])
	invokes      = [c for c in parameters[1]]
	
	C = {}
	O = {}
	
	for j in range(0, num_combines):
		a = combines[j][0]
		b = combines[j][1]
		c = combines[j][2]
		d = [a, b]		
		d.sort()
		if d[0] in C:
			C[d[0]][d[1]] = c
		else:
			C[d[0]] = {
				d[1] : c
			}
		
	for j in range(0, num_opposed):
		a = opposed[j][0]
		b = opposed[j][1]
		d = [a, b]		
		d.sort()
		if d[0] in O:
			O[d[0]][d[1]] = True
		else:
			O[d[0]] = {
				d[1] : True
			}

	#print("Combines %s" % combines)
	#print("Opposed  %s" % opposed)
	invoked = []
	if len(invokes) > 0:
		invoked.append(invokes[0])
		for j in range(1, num_invokes):
			invoked.append(invokes[j])
			if len(invoked) > 1:
				prev = invoked[-2]
				next = invoked[-1]
				a = [prev, next]
				a.sort()
				a0 = a[0]
				a1 = a[1]
				if a0 in C:
					if a1 in C[a0]:
						new_element = C[a0][a1]
						del invoked[-1]
						del invoked[-1]
						invoked.append(new_element)
						continue
				for c in invoked[:-1]:
					a = [c, next]
					a.sort()
					a0 = a[0]
					a1 = a[1]
					if a0 in O:
						if a1 in O[a0]:
							invoked[:] = []
							break
	output_string = ""
	if len(invoked) > 0:
		output_string = invoked[0]
		for j in range(1, len(invoked)):
			output_string += ", %s" % invoked[j]
	print("Case #%d: [%s]" % (i + 1, output_string))
