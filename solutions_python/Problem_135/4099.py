import sys

f = open("A-small-attempt3.in.txt")

testc = f.readline()

for t in range(0,int(testc)):
	r = int(f.readline())
	l1 = f.readline().strip().split(' ')
	l2 = f.readline().strip().split(' ')
	l3 = f.readline().strip().split(' ')
	l4 = f.readline().strip().split(' ')
	c = int(f.readline())
	r1 = f.readline().strip().split(' ')
	r2 = f.readline().strip().split(' ')
	r3 = f.readline().strip().split(' ')
	r4 = f.readline().strip().split(' ')
	l = [l1,l2,l3,l4]
	n = [r1,r2,r3,r4]
	s = set(l[r-1]) & set(n[c-1])
	if len(s) > 1:
		print ("Case #%d: Bad magician!")%(t+1)
	if len(s) == 1:
		print ("Case #%d: %d")%(t+1,int(list(s)[0]))
	if len(s) == 0:
		print ("Case #%d: Volunteer cheated!")%(t+1)

f.close()	
