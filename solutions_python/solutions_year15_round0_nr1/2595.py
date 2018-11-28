import sys
sOrl = sys.argv[1]

inputs = open("qualifier_a_%sinput.txt" %(sOrl)).readlines()

num = int(inputs[0])
cases = []
for i in range(1,num+1):
	case = inputs[i].strip().split(" ")
	cases.append(case[-1])

fout = open("qualifier_a_%soutput.txt" %(sOrl), "w")
for i in range(len(cases)):
	added = 0
	standing = int(cases[i][0])
	for j in range(1,len(cases[i])):
		if standing < j:
			added += j - standing
			standing += j - standing
		standing += int(cases[i][j])
	fout.write("Case #%d: %d\n" %(i+1, added))
fout.close()
		