#!/usr/bin/python
import sys

finput = sys.argv[1]
fi = open(finput)
num = int(fi.readline())

def process(seq, com, opp):
	new_seq = []
	for i in seq:
		cleaned = False
		if len(new_seq) == 0:
			new_seq += [i]
		elif new_seq[-1]+i in com:
			new_seq[-1] = com[new_seq[-1]+i]
		else:
			if i in opp:
				for j in opp[i]:
					if j in new_seq:
						new_seq = []
						cleaned = True
						break
			if not cleaned:
				new_seq += [i]
	return new_seq

for i in range(num):
	tmp = fi.readline().strip("\n").split()
	C = int(tmp[0])
	combinations = tmp[1:C+1]
	com_dict = {}
	for com in combinations:
		com_dict[com[0]+com[1]]=com[2]
		com_dict[com[1]+com[0]]=com[2]
	D = int(tmp[C+1])
	oppositions = tmp[(C+2):(C+D+2)]
	opp_dict = {}
	for opp in oppositions:
		if opp[0] in opp_dict: opp_dict[opp[0]]+=opp[1]
		else: opp_dict[opp[0]]=opp[1]
		if opp[1] in opp_dict: opp_dict[opp[1]]+=opp[0]
		else: opp_dict[opp[1]]=opp[0]

	sequence = tmp[C+D+3]

	res = process(sequence, com_dict, opp_dict)
	print ("Case #%i: %s") % (i+1, res)
