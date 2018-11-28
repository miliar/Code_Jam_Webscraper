f = open( "file1.in", "r" )
of = open("Output.out", "w")
lines = f.readlines()
case_count = int(lines[0])
cx = 1
cc = 0
for c in range(0, case_count):
	cc += 1
	answer1 = int(lines[cx+0].strip())
	line1 = lines[cx+answer1].strip().split(" ")
	la1 = []
	for c in line1:
		la1.append(int(c))
	answer2 = int(lines[cx+5].strip())
	line2 = lines[cx+5+answer2].strip().split(" ")
	la2 = []
	for c in line2:
		la2.append(int(c))
	cx += 10
	match = [x for x in la1 if x in la2]
	if len(match) > 1:
		of.write("Case #%d: Bad magician!\n" % (cc))
		print "Case #%d: Bad magician!" % (cc)
	elif len(match) == 0:		
		of.write("Case #%d: Volunteer cheated!\n" % (cc))
		print "Case #%d: Volunteer cheated!" % (cc)
	else:
		of.write("Case #%d: " % (cc))
		of.write("%d\n" % match[0])
		print "Case #%d:" % (cc),
		print match[0]
f.close()
of.close()
