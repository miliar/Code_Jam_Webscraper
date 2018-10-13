
import sys

current_line = 0

data = open("A-small-attempt0.in","r").readlines()

def seek(pos):
	global current_line
	current_line = pos
	
def read_current_line():
	global current_line
	tmp = current_line
	current_line = current_line + 1
	return data[tmp]
	
test_case_count = int(read_current_line())

for i in range(test_case_count):
	
	q1 = int(read_current_line())

	s1 = set()
	for j in range(4):
		line = read_current_line()
		if j==(q1-1):
			nums = line.split()
			for n in nums:
				s1.add(int(n))
	s2 = set()
	q2 = int(read_current_line())
	for j in range(4):
		line = read_current_line()
		if j == (q2-1):
			nums = line.split()
			for n in nums:
				s2.add(int(n))
	
	res = s1.intersection(s2)
	
	if len(res) == 1:
		print "Case #" + str(i+1) + ": " + str(res.pop())
	elif len(res) > 1:
		print "Case #" + str(i+1) + ": Bad magician!"
	elif len(res) == 0:
		print "Case #" + str(i+1) + ": Volunteer cheated!"
		
	# print "looking at case", i, "q1", q1, "q2", q2, s1, s2,
	# print s1.intersection(s2)
	
		
	