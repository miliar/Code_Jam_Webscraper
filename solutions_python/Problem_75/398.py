#!/usr/bin/python
from string import atoi
from sys import argv 

def solve(inputfile):
	f = open(inputfile, "r")
	cases = atoi(f.readline())	
	for case in range(cases):
		cdata = f.readline()
		cdata = cdata.split()
		cdata.reverse()

		C = {} 
		D = {} 

		cnum = atoi(cdata.pop())
		for cn in range(cnum):
			cd = cdata.pop()
			C[cd[:2]] = cd[2:]
			C[cd[:2][1] + cd[:2][0]] = cd[2:]

		dnum = atoi(cdata.pop())
		for dn in range(dnum):
			dd = cdata.pop()
			if D.has_key(dd[0]):
				D[dd[0]].append(dd[1])
			else: D[dd[0]] = [dd[1]]

			if D.has_key(dd[1]):
				D[dd[1]].append(dd[0])
			else: D[dd[1]] = [dd[0]]


		N = cdata.pop()
		N = cdata.pop()
		dlist = []	
		output = ""	
		last_added = []
		for x in range(len(N)):
			if output != "" and C.has_key(output[-1] + N[x]):
				l = output[-1]
				output = output[:-1]
				output += C[l + N[x]]
				if D.has_key(l):	
					for y in D[l]:
						dlist.remove(y)

			else: output += N[x]

			if D.has_key(output[-1]):
				for y in D[output[-1]]:
					dlist.append(y)
					last_added.append(y)
			else:
				last_added = []

			if output[-1] in dlist:
				output = ""
				dlist = []

		output = str(list(output)).replace("'","")
		print "Case #%d: %s"%(case+1, str(output))
			
if __name__ == "__main__": solve(argv[1])
