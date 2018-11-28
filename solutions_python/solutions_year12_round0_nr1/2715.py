f = open('A-small-attempt1.in', 'r')
lines = f.readlines()
f.close()
f = open('output.txt', 'a')
for line in lines[1:]:
	new_line = line.replace('y', 'A').replace('e', 'O').replace('q', 'Z').replace('j', 'U').replace('p', 'R').replace('m', 'L').replace('s', 'N').replace('l', 'G').replace('c', 'E').replace('k', 'I').replace('s', 'D').replace('k', 'I').replace('x', 'M').replace('v', 'P').replace('d', 'S').replace('n', 'B').replace('r', 'T').replace('i', 'D').replace('h', 'X').replace('b', 'H').replace('t', 'W').replace('a', 'Y').replace('w', 'F').replace('f', 'C').replace('o', 'K').replace('u', 'J').replace('g', 'V').replace('z', 'Q')
	f.write('Case #%d: %s' % (lines.index(line), new_line.lower()))
f.close()