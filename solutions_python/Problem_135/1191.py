import numpy as np

filen = 'in'
with open(filen) as f:
	content = f.readlines()

content = [i.strip() for i in content]

testn = 1
for i in np.arange(1, len(content)-1, 10):
	row1 = int(content[i])
	row2 = int(content[i + 5])
	options1 = np.array(content[i + row1].split(" "))
	options2 = np.array(content[i + 5 + row2].split(" "))
	ans = np.in1d(options1, options2)
	if sum(ans) == 1:
		print "Case #%d: %s" % (testn, options1[ans][0])
	elif sum(ans) >= 2:
		print "Case #%d: Bad magician!" % testn
	else:
		print "Case #%d: Volunteer cheated!" % testn
	testn += 1
