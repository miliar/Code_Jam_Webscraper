def standing():
	fname = 'A-small-attempt0.in'
	content = [line.strip() for line in open(fname)]
	numLines = content[0]
	content = content[1:]
	#print numLines
	#print content
	for i in range(len(content)):
		content[i] = content[i][2:]
	#print content
	k = 0

	f = open('output.txt','w')

	for i in content:
		k += 1
		extras = 0
		totalUp = 0
		for j in range(len(i)):
			if j <= totalUp:
				totalUp += int(i[j])
			if j > totalUp and int(i[j]) != 0:
				extras += j - totalUp
				totalUp += j - totalUp + int(i[j])
			#print totalUp
			#print extras
		f.write('Case #' + str(k) + ': ' + str(extras))
		f.write('\n')

	f.close()

standing()
