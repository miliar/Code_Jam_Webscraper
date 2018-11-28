#!/usr/bin/python
import sys
from pprint import pprint

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')
	
	for case in xrange(1, int(infile.readline())+1):
		input = infile.readline().split()
		elist = []
		
		# register combinations
		ncombis = int(input[0])
		combis = dict((combi[:-1], combi[-1:]) for combi in input[1:(ncombis+1)])
		
		# register conflicts
		nconflicts = int(input[ncombis+1])
		conflicts = input[(ncombis+2):-1]
		
		# process raw casts
		raw = input[-1]
		for element in raw:
			elist.append(element)
			if len(elist)<2: continue
			#build combinations
			lasttwo = "".join(elist[-2:])
			if not lasttwo in combis:
				lasttwo = lasttwo[1] + lasttwo[0]
			if lasttwo in combis:
				elist = elist[:-2]
				elist.append(combis[lasttwo])
			
			# check for conflicts
			for conflict in conflicts:
				if conflict[0] in elist and conflict[1] in elist:
					elist = []
		
		outfile.write("Case #%i: [%s]\n"%(case, ", ".join(elist)))
	
	

if __name__ == "__main__":
	main()
