f = open("/Users/mklein16/Desktop/gcj/A-small-attempt0.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")
for i in range(cases):
	content = []
	for a in range(10):
		content.append(contents[1+a+i*10])
	rowa = int(content[0])
	rowb = int(content[5])
	contenta = content[1:5]
	contentb = content[-4:]
	ra = contenta[rowa-1].split(" ")
	rb = contentb[rowb-1].split(" ")
	for x in range(len(rb)):
		ra.append(rb[x])
	c = 0

	val = "Volunteer cheated!"
	for x in range(len(ra)):
		if ra.count(ra[x]) == 2: 
			c+=1
			val = ra[x]
	if c > 2:
		val = "Bad magician!"
	f.close()
	g = open("/Users/mklein16/Desktop/gcj/output.txt", 'a')
	g.write("Case #" + `i+1`+": " + val + "\n")
	g.close()