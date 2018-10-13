import sys
from sets import Set
def read_board():
	configuration = []
	for i in range(0, 4):
		configuration = configuration + [[int(j) for j in raw_input().split()]]
	return configuration
path = ""
name = "A-small-attempt0"
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")
tc = input()
for cc in range(1, tc + 1):
	firstRow = input()
	firstConfig = read_board()
	secondRow = input()
	secondConfig = read_board()
	a = set(firstConfig[firstRow-1])
	b = set(secondConfig[secondRow-1])
	c = a.intersection(b)
	if(len(c)>1):
		print 'Case #'+str(cc)+': '+'Bad magician!'
	elif(len(c)==0):
		print 'Case #'+str(cc)+': '+'Volunteer cheated!'
	else:
		print 'Case #'+str(cc)+ ': '+str(c.pop())


