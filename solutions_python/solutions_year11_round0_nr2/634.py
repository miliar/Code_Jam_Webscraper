import sys

def main():

	data = sys.stdin.read().split("\n")
	nbTest = int(data[0])
	data.pop(0)

	for i in xrange(0, nbTest):
		print "Case #%s: %s" % (i+1, sequence(data[0]))
		data.pop(0)


def sequence(seq):
	
	seq = seq.split(" ")

	C = int(seq[0])
	combinations = seq[1:C+1]
	
	# list of possible combination
	base = [x[:2] for x in combinations]
	non_base = [x[-1] for x in combinations]


	D = int(seq[C+1])
	opposed = seq[C+2:D+C+2]

	# list of opposed elements
	opp = []
	
	for o in opposed:
		opp.append(o[0])
		opp.append(o[1])

	
	N = int(seq[D+C+2])

	# elements to "invoke"
	elements = list(seq[D+C+3:D+C+3+N][0])

	element_list = []


	for e in elements:
		# add elements
		element_list.append(e)

		# check combination
		if (len(element_list) > 1) and (element_list[-1]+element_list[-2] in base):
			index = base.index(element_list[-1]+element_list[-2])
			del element_list[-1]
			del element_list[-1]
			element_list.append(non_base[index])
		elif (len(element_list) > 1) and (element_list[-2]+element_list[-1] in base):
			index = base.index(element_list[-2]+element_list[-1])
			del element_list[-1]
			del element_list[-1]
			element_list.append(non_base[index])

		# check opposed
			
		if (len(element_list) > 1) and (element_list[-1] in opp):
			tmp = opp.index(element_list[-1])
			if (tmp % 2 == 0) and (opp[tmp+1] in element_list):
				element_list = []
			elif (not (tmp % 2 == 0)) and (opp[tmp-1] in element_list):
				element_list = []
		

	# format output
	res = "["
	for e in element_list:
		res += e + ", "
	if len(res) > 2:
		res = res[0:-2]
	res += "]"
	return res
					

main()
