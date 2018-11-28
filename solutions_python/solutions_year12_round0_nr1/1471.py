filename = 'A-small-attempt0.in'
out_file = 'output.txt'
text = open(filename, "r")

line_counter = 1
output = ''
for line in text:
	if line_counter == 1:
	    testcase_num = line
	else:
	    output += 'Case #'+str(line_counter-1)+': '
	    input_text = line
	    for ch in input_text:
		if ch == 'y':
		    output += 'a'
		elif ch == 'n':
		    output += 'b'
		elif ch == 'f':
		    output += 'c'
		elif ch == 'i':
		    output += 'd'
		elif ch == 'c':
		    output += 'e'
		elif ch == 'w':
		    output += 'f'
		elif ch == 'l':
		    output += 'g'
		elif ch == 'b':
		    output += 'h'
		elif ch == 'k':
		    output += 'i'
		elif ch == 'u':
		    output += 'j'
		elif ch == 'o':
		    output += 'k'
		elif ch == 'm':
		    output += 'l'
		elif ch == 'x':
		    output += 'm'
		elif ch == 's':
		    output += 'n'
		elif ch == 'e':
		    output += 'o'
		elif ch == 'v':
		    output += 'p'
		elif ch == 'z':
		    output += 'q'
		elif ch == 'p':
		    output += 'r'
		elif ch == 'd':
		    output += 's'
		elif ch == 'r':
		    output += 't'
		elif ch == 'j':
		    output += 'u'
		elif ch == 'g':
		    output += 'v'
		elif ch == 't':
		    output += 'w'
		elif ch == 'h':
		    output += 'x'
		elif ch == 'a':
		    output += 'y'
		elif ch == 'q':
		    output += 'z'
		else:
		    output += ch
		
	line_counter += 1

out = open(out_file, "w")
out.write(output)
