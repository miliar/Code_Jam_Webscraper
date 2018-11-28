import csv, snapper

reader = csv.reader(open('/home/elmoss/Desktop/A-small-attempt1.in'), delimiter = ' ')
lines = []
for line in reader:
	row = []
	for item in line:
		row.append(int(item))
	lines.append(row)
lines = lines[::-1]
results = []
for trial in range(0, lines.pop()[0]):
	trialspecs = lines.pop()
	snappers = trialspecs[0]
	snaps = trialspecs[1]
	train = snapper.snapperTrain(snappers)
	bulb = train.getBulb()
	print 'performing trial ' + str(trial) + ' with specs:'
	print trialspecs
	for snap in range(0, snaps):
		bulb.snap()
	if bulb.isOn():
		print 'LIGHT'
		results.append('Case #' + str(trial+1)+': ON\n')
	else:
		print 'NO LIGHT'
		results.append('Case #' + str(trial+1)+': OFF\n')

#print results
outfile = open('/home/elmoss/Desktop/outfile.txt', 'w')
for item in results:
	outfile.write(item)
outfile.close()