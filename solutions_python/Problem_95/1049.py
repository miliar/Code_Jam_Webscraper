import string

map = {}
for char in string.lowercase:
	map[char] = ''
map[' '] = ' '
map['y'] = 'a'
map['e'] = 'o'
map['q'] = 'z'
input_lines = []
input_lines.append('ejp mysljylc kd kxveddknmc re jsicpdrysi')
input_lines.append('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
input_lines.append('de kr kd eoya kw aej tysr re ujdr lkgc jv')
output_lines = []
output_lines.append('our language is impossible to understand')
output_lines.append('there are twenty six factorial possibilities')
output_lines.append('so it is okay if you want to just give up')

num_lines = len(input_lines)
for i in xrange(num_lines):
	input_line = input_lines[i]
	output_line = output_lines[i]
	for j in xrange(len(input_line)):
		ichar = input_line[j]
		jchar = output_line[j]
		if map[ichar] == '':
			map[ichar] = jchar
		elif not(map[ichar] == jchar):
			print ichar, map[ichar], jchar
for char in string.lowercase:
	found = False
	for key in map.keys():
		if char == map[key]:
			found = True
			break
	if found == False: 
		map['z'] = char
length = int(raw_input().strip())	
for i in xrange(length):
	line = raw_input().strip()
	print 'Case #%s:' % (i+1),
	output_string = ''
	for char in line:
		output_string = output_string + map[char]
	print output_string