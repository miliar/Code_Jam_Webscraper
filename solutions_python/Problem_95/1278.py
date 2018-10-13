#!/usr/bin/python
#coding=utf-8
import sys

char_dict = {' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'}

if len(sys.argv) < 3:
	print "Uso: %s <input filename> <output filename>" % sys.argv[0]
	sys.exit()
input_filename = sys.argv[1]
output_filename = sys.argv[2]
file = open(input_filename, "r")
output_file = open(output_filename, "w")
cases = int(file.readline())

for case in range(0,cases):
	whole_line = file.readline()
	new_str = []
	for i in range(0, len(whole_line)-1):
		new_str.append(char_dict[whole_line[i]])
	result = ''.join(new_str)
	output_file.write('Case #%d: %s\n' % (case+1, result))

file.close()
output_file.close()

