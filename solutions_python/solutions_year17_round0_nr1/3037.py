f = open("input.in", "r")
out = open("out.out", "w")

cases = int(f.readline())
num = 0
good = True
for line in f:
        good = True
	num+=1
	splits = line.split(" ")
	row = splits[0]
	k = int(splits[1])
	flips = 0
	for i in range(len(row)):
		if i+k >len(row):
			break
		if row[i]=='+':
			continue
		flips+=1
		for j in range(k):
			if row[i+j]=='-':				
				row = row[:i+j]+ '+' + row[i+j+1:]
			else:
                                row = row[:i+j]+ '-' + row[i+j+1:]
	
	for c in row:
		if c!='+':
			good = False
			
	if good:
		out.write("CASE #%d: %d\n" % (num, flips))
	else:
		out.write("CASE #%d: IMPOSSIBLE\n" % (num))
out.close()
f.close()
