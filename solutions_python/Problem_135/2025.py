'''
Problem A: Magic Trick
@author: peggyli
'''

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange(1, t+1):
		row1 = int(raw_input())
		grid1 = []
		for k in xrange(4):
			grid1.append(raw_input().split())

		row2 = int(raw_input())
		grid2 = []
		for k in xrange(4):
			grid2.append(raw_input().split())

		common = [card for card in grid1[row1-1] if card in grid2[row2-1]]

		if len(common) == 1:
			print "Case #%d: %s" % (i, common[0])
		elif len(common) > 1:
			print "Case #%d: Bad magician!" % i
		elif len(common) == 0:
			print "Case #%d: Volunteer cheated!" % i