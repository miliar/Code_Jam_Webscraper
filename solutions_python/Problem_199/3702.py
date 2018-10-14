import sys

def first_blank(pancakes):
    for i in xrange(len(pancakes)):
        if pancakes[i] == '-':
	    return i
    return -1	

def flip(pancakes, size):
    for i in xrange(len(pancakes)):
        if pancakes[i] == '-':
            j = 0;
	    while (j < size):
		if pancakes[i + j] == '-':
		    pancakes[i + j] = '+'
		else:
		    pancakes[i + j] = '-'
		j = j + 1
	    break		
    return pancakes
            
cases = int(raw_input())
for case in xrange(1, cases + 1):
    pancakes, size = raw_input().split()
    pancakes = list(pancakes)
    size = int(size)
    steps = 0
    while True:
        fb = first_blank(pancakes)
        if fb == -1:
	    print "Case #%d: %d" % (case, steps)
	    break	
	elif fb + size > len(pancakes):
	    print "Case #%d: IMPOSSIBLE" % (case)
 	    break
	steps = steps + 1
	pancakes = flip(pancakes, size)



