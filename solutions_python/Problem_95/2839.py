import sys
import string

file_in = open('A-small-attempt2.in', 'r')
file_out = open('A-small-attempt2_out.in', 'w')

num_cases = file_in.readline()
print 'Number of cases: ', num_cases

g_to_en = {'y': 'a', 'e': 'o', 'q': 'z'}

def translate(text):
	output = ''
	for c in text:
		if c in g_to_en:
			output += g_to_en[c]
		else:
			output += c
	return output

lines_i = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']
lines_o = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']

for i in range(len(lines_i)):
	line = lines_i[i]
	for j in range(len(line)):
		c = line[j]
		g_to_en[c] = lines_o[i][j]

k = 1
print g_to_en
g_to_en['z'] = 'q'
for line in file_in:
	file_out.write('Case #' + str(k) + ': ' + translate(line))
	k += 1

for kv in g_to_en:
	print kv