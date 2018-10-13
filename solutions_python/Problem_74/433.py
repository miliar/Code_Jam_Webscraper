import math

#f = file("problem1test.in", "r")
#f = file("/Users/finn/Downloads/A-small-attempt0.in", "r")
f = file("/Users/finn/Downloads/A-large.in", "r")
#of = file("A-small.out", "w")
of = file("A-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
line = 1
for case in range(cases):
	data = lines[line].split()
	presses = int(data[0])
	
	seq = []
	for p in range(presses):
		seq.append((data[p * 2 + 1], int(data[p * 2 + 2])))

	b_pos = 1
	o_pos = 1

	result = 0
	while len(seq) > 0:
		if seq[0][0] == 'O':
			dist = abs(o_pos - seq[0][1])
			
			next_b_pos = b_pos
			for s in seq:
				if s[0] == 'B':
					next_b_pos = s[1]
					break
					
			if b_pos < next_b_pos:
				b_pos += dist + 1
				if b_pos > next_b_pos:
					b_pos = next_b_pos
				
			if b_pos > next_b_pos:
				b_pos -= dist + 1
				if b_pos < next_b_pos:
					b_pos = next_b_pos
					
			result += dist + 1
			o_pos = seq[0][1]
		else:
			dist = abs(b_pos - seq[0][1])
			
			next_o_pos = o_pos
			for s in seq:
				if s[0] == 'O':
					next_o_pos = s[1]
					break
					
			if o_pos < next_o_pos:
				o_pos += dist + 1
				if o_pos > next_o_pos:
					o_pos = next_o_pos
				
			if o_pos > next_o_pos:
				o_pos -= dist + 1
				if o_pos < next_o_pos:
					o_pos = next_o_pos
					
			result += dist + 1
			b_pos = seq[0][1]
			
		seq = seq[1:]
		
	of.write("Case #%d: %d\n" % (case + 1, result))
		
	#of.write("Case #%d: %d\n" % (case + 1, total))
	
	line += 1