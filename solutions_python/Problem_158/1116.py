testcases = int(raw_input())
for i in range(testcases):
	brikke, x, y = raw_input().split(' ')
	brikke = int(brikke)
	x = int(x)
	y = int(y)
	brett = x*y
	if brikke > brett:
		print "Case #" + str(i+1) + ": RICHARD"
		continue
	if brikke == 4 and brett == 2*4:
		print "Case #" + str(i+1) + ": RICHARD"
		continue
	if(brikke ==1):
		print "Case #" + str(i+1) + ": GABRIEL"
		continue
	elif(brikke == 2):
		if (not(brett%brikke == 0)):
			print "Case #" + str(i+1) + ": RICHARD"
		else:
			print "Case #" + str(i+1) + ": GABRIEL"

	elif(brikke == 3):
		if x == 1 or y == 1:
			print "Case #" + str(i+1) + ": RICHARD"
		elif (not(brett%brikke == 0)):
			print "Case #" + str(i+1) + ": RICHARD"
		else:
			print "Case #" + str(i+1) + ": GABRIEL"

	elif(brikke == 4):
		if x == 1 or y == 1:
			print "Case #" + str(i+1) + ": RICHARD"
		elif(not(x==4 or y == 4)):
			print "Case #" + str(i+1) + ": RICHARD"
		elif (not(brett%brikke == 0)):
			print "Case #" + str(i+1) + ": RICHARD"
		else:
			print "Case #" + str(i+1) + ": GABRIEL"



