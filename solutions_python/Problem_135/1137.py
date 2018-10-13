#import math

sourcepath = '/Users/alistairpalfreyman/Documents/Code Jam/Input/A-small-attempt0.in.txt'
destpath = '/Users/alistairpalfreyman/Documents/Code Jam/Output/A-small-attempt0.out.txt'

def solve(s1, r1, s2, r2):
	
	combos = [0] * 16
	
	for row in range(4):
		for col in range(4):
			combos[r1[row][col]-1] = str(row+1)
	
	for row in range(4):
		for col in range(4):
			combos[r2[row][col]-1] += str(row+1)
	
	selection = s1.rstrip() + s2.rstrip()
	hits = [x for x in combos if x == selection]
	
	if len(hits) == 0:
		result = 'Volunteer cheated!'
	elif len(hits) == 1:
		result = str(combos.index(selection) + 1)
	else:
		result = 'Bad magician!'
	
	return result
	



fd = open(sourcepath, 'r')
fo = open(destpath, 'w')
T = int(fd.readline())
for i in range(1,T+1):
	select1 = fd.readline()
	rows1 = [[int(a) for a in fd.readline().split(' ')] for x in xrange(4)]
	
	select2 = fd.readline()
	rows2 = [[int(a) for a in fd.readline().split(' ')] for x in xrange(4)] 
	
	result = solve(select1, rows1, select2, rows2)
	
	print 'Case #' + str(i) + ': ' + result + '\n',
	fo.write('Case #' + str(i) + ': ' + result + '\n')
	
fd.close()
fo.close()


	