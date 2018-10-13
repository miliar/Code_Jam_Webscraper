
mapping = "ynficwlbkuomxsevzpdrjgthaq"

for case in range(1,int(raw_input())+1):
	line = raw_input()
	result = ""
	for i in range(len(line)):
		if(line[i]==" "): result+=" "
		else: result+=chr(mapping.index(line[i])+97)
	print "Case #"+str(case)+": "+result