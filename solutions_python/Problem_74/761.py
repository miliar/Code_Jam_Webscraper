import sys

def parse_line(line):
    tokens = line.split()
    i = 0
    o = ['O', 1, []]
    b = ['B', 1, []]
    order = []
    while i/2 < int(tokens[0]):
       	if tokens[i+1] == "O":
       		o[2].append(int(tokens[i+2]))
       	elif tokens[i+1] == "B":
       		b[2].append(int(tokens[i+2]))
       	order.append(tokens[i+1])
       	i += 2
    return o, b, order

def solve(i, o, b, order):
    count = 0
    pushed = False
    while True:
       	if pushed:
       		order = order[1:]
       		pushed = False
       	if len(order) > 0:
       		for r in (o, b):
       			if len(r[2]) > 0:
       				if r[1] < r[2][0]:
       					r[1] += 1
       					#print "%s move to button %d" % (r[0], r[1])	
				elif r[1] > r[2][0]:
						r[1] -= 1
						#print "%s move to button %d" % (r[0], r[1])
	       			else:
	       				if r[0] == order[0]:
	       					r[2] = r[2][1:]
	       					pushed = True
	       					#print "%s push button %d" % (r[0], r[1])
        else:
	       	print "Case #%d: %d" % (i, count)
	       	return
        count += 1

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    tests = int(lines[0])
    i = 0
    while i < tests:
        solve(i+1, *parse_line(lines[i+1]))
        i+=1