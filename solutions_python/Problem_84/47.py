def testCase():
	rows, columns = (int(n) for n in raw_input().split())
	image = [raw_input() for _ in xrange(rows)]
	for row in xrange(rows - 1):
		blue = image[row].find("##")
		while blue != -1:
			if image[row+1][blue:blue+2] != "##":
				return
			image[row] = image[row][:blue] + "/\\" + image[row][blue+2:]
			image[row+1] = image[row+1][:blue] + "\\/" + image[row+1][blue+2:]
			blue = image[row].find("##")
		if "#" in image[row]:
			return
	if "#" in image[rows - 1]:
		return
	return image

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d:" % (i+1)
		s = testCase()
		if s is None:
			print "Impossible"
		else:
			for line in s:
				print line
