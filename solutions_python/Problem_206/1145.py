#encoding=utf8
filename = "A-large.in"
raw_data = ''
with open(filename, 'r') as f:
	raw_data = f.read().split('\n')

test_count = int(raw_data.pop(0))
for test in range(test_count):
	question = raw_data.pop(0).split(' ')

	meters = int(question.pop(0))
	hourses = int(question.pop(0))
	miniTime = 0

	for hcount in range(hourses):
		curD = raw_data.pop(0).split(' ')
		hposition = int(curD.pop(0))
		hspeed = int(curD.pop(0))
		if miniTime < ((meters - hposition)/hspeed) :
			miniTime = ((meters - hposition)/hspeed)


	if miniTime != 0 :
		print "Case #%d: %.6f"%(test+1,float(meters)/miniTime)
	else:
		print "Case #%d: %.6f"%(test+1,float(meters))
	#print "%.2f kg = %.2f lb = %.2f gal = %.2f l" % (var1, var2, var3, var4)