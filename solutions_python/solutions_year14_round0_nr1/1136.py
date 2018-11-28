import io

def main():
	stream = open("magic-trick.in")
	output = open("magic-trick-ans.txt", mode='w')
	tests = int(stream.readline())
	for i in xrange(tests):
		num = -1
		board1 = []
		candidates = []
		row1 = int(stream.readline())
		for j in xrange(4):
			board1.append(stream.readline().split(" "))
		for j in xrange(4):
			candidates.append(int(board1[row1-1][j]))
		print candidates
		board1 = []
		row2 = int(stream.readline())
		for j in xrange(4):
			board1.append(stream.readline().split(" "))
		for j in xrange(4):
			if int(board1[row2-1][j]) in candidates:
				if(num == -1):
					num = int(board1[row2-1][j])
				else:
					num = -2
					output.write("Case #%d: Bad magician!\n" % (i+1))
					break
		if(num == -2):
			continue
		if(num != -1):
			output.write("Case #%d: %d\n" % (i+1, num))
		else:
			output.write("Case #%d: Volunteer cheated!\n" % (i+1))

main()