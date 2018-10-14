#!/usr/bin/python

def solve():
    line = raw_input().split()
    n = int(line[0])
    p = int(line[1])
    g = int(line[2])
    
    for i in range(1, n + 1):   
	if g == 100:
		if p == 100: return 'Possible'
		else: continue
	elif g == 0:
		if p != 0: continue
		else: return 'Possible'
 	
    	tmp = i * (p / 100.0)
	p_number = int(tmp)
	#print tmp, p_number
	if (tmp - p_number) != 0: continue

	g_number = i / (1 - (g / 100.0))
	#print g_number, i, g
	if g_number != 0 and g_number >= p_number and g_number >= i:
		return 'Possible'
    
    return 'Broken'

	
for i in range(input()):
    print "Case #%d: %s" % (i+1, solve())
    
    
