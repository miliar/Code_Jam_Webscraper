def analyze_line(line):
    o_lines = []
    b_lines = []
    order = []
    line = line.split(' ')
    count = int(line.pop(0))
    i = 0
    while i < count:
	a = line.pop(0)
	b = int(line.pop(0))
	
	if(a == 'O'):
	    #print "O move %i: %s %s" % (i, a, b)
	    order.append(a)
	    o_lines.append(b)
	else:
	    #print "B move %i: %s %s" % (i, a, b)
	    order.append(a)
	    b_lines.append(b)
	    
	i += 1
	
    return(order, o_lines, b_lines)

def solve_line(order, o, b):
    o_idx = 1
    b_idx = 1
    moves = 0

    while len(o) != 0 or len(b) != 0:
	pushed = False
	if len(o) > 0:
	    if o_idx == o[0]:
		if order[0] == 'O':
		    o.pop(0)
		    order.pop(0)
		    pushed = True
	    else:
		if o_idx > o[0]:
		    o_idx -= 1
		else:
		    o_idx += 1

	if len(b) > 0:
	    if b_idx == b[0]:
		if order[0] == 'B' and pushed == False:
		    b.pop(0)
		    order.pop(0)
	    else:
		if b_idx > b[0]:
		    b_idx -= 1
		else:
		    b_idx += 1
	    
	moves += 1

    return moves
    
f = open('A-large.in', 'r');
def strip(x): return x.rstrip()
lines = map(strip, f.readlines())
count = int(lines[0])

i = 0
while i < count:
    i += 1
    (order, o, b) = analyze_line(lines[i])
    result = solve_line(order, o, b)
    print "Case #%i: %i" % (i, result)
    


    
