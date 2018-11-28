import sys

def solveline(line, case):
	combis = int(line[0])
	combilist = dict([("".join(sorted(i[0:2])),i[2]) for i in line[1:combis+1]])
	anni = int(line[combis+1])
	annilist = ["".join(sorted(i)) for i in line[combis+2:combis+2+anni]]
	outputli = []
	for char in line[-1]:
		#check for combinations first
		if not outputli:
			outputli.append(char)
			continue
		replacement = combilist.get("".join(sorted(char+outputli[-1])),"")
		if replacement:
			outputli[-1] = replacement
			continue
		#check for annihilations
		for i in range(len(outputli)):
			if "".join(sorted(char+outputli[i])) in annilist:
				outputli = []
				break
		else:
			outputli.append(char)
	print "Case #%s: [%s]" % (case, ", ".join(outputli))

with open(sys.argv[1]) as fp:
	lines = int(fp.readline())
	for i in range(1,lines+1):
		line = fp.readline().strip().split()
		solveline(line, i)
