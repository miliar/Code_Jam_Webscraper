import re
f = open("input.txt", "r")
fout = open("output.txt", "w")

case = 0
for line in f:
	if case == 0:
		case+=1
		continue
	
	lineA = line.split(" ")
	combine = []
	oppose = []
	i = 0

	if int(lineA[i]) == 0:
		i += 1
	else:
		for n in range(0, int(lineA[i])):
			combine.append(lineA[i + 1 + n])
		i += 1 + int(lineA[i]) 
	
	if int(lineA[i]) == 0:
		i += 1
	else:
		for n in range(0, int(lineA[i])):
			oppose.append(lineA[i + 1 + n])
		i += int(lineA[i]) + 1

	invoke = lineA[i + 1].strip()
	elements = ""
	i = 0	
	while i <= len(invoke) - 1:
		elements += invoke[i]

		l = len(elements) - 1 
		for let in combine:
			if l != 0 and (elements[l] == let[0] and elements[l-1] == let[1]):
				elements = elements[0:l-1]
				elements = elements + let[2]
				l = len(elements) - 1
			elif l != 0 and (elements[l] == let[1] and elements[l-1] == let[0]):
				elements = elements[0:l-1]
				elements = elements + let[2]
				l = len(elements) - 1

		#	if (elements[i] == let[0] and elements[i+1] == let[1]):
		#		elements = elements.replace(elements[i] + elements[i+1], let[2], 1)
		#	elif (elements[i] == let[1] and elements[i+1] == let[0]):
		#		elements = elements.replace(elements[i] + elements[i+1], let[2], 1, )
		l = len(elements) - 1 
		for let in oppose:
		#	if elements[i] == let[0]:
		#		e = re.sub(let[0]+ r".*?" + let[1], '', elements, 1)
		#		if e != elements:
		#			elements = e
		#			i-=1
		#	if i >= len(elements) - 1:
		#		continue
		#	if elements[i] == let[1]:
		#		e = re.sub(let[1]+ r".*?" + let[0], '', elements, 1)
		#		if e != elements:
		#			elements = e
		#			i-=1
			if l != 0 and elements[l] == let[0]:
				if elements.find(let[1]) != -1:
					elements = ""
					l = 0
			if l != 0 and elements[l] == let[1]:
				if elements.find(let[0]) != -1:
		 			elements = ""
					l = 0
		i+=1
	output = '['
	for l in elements:
		output += l + ', '
	
	if len(output) > 1:
		output = output[0:len(output)-2]
	output += ']'
	fout.write("Case #" + str(case) + ": " + output + "\n")
	
	case+=1
