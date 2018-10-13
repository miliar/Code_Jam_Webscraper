
def solve():
	ntest = int(raw_input())
	for i in range(0, ntest):
		r1 = int(raw_input())
		row1 = set()
		for j in range(0,4):
			t = raw_input()
			if j+1 == r1:
				t = t.split(" ")
				for ele in t:
					row1.add(int(ele))
		r2 = int(raw_input())
		row2 = set()		
		for j in range(0,4):
			t = raw_input()
			if j+1 == r2:
				t = t.split(" ")
				for ele in t:
					row2.add(int(ele))
		row1 = set.intersection(row1,row2)
		if len(row1) == 1:
			result = 0
			for ele in row1:
				result = ele
			print "Case #%d: %d" % (i+1,ele)
		elif len(row1) == 0:
			print "Case #%d: Volunteer cheated!" % (i+1)
		else:
			print "Case #%d: Bad magician!" % (i+1)

if __name__ == "__main__":
	solve()
