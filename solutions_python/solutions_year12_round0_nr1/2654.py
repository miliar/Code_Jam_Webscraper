#!/usr/bin/env python

import os

source = open('A-small-attempt3.in','r')
destination = open('A-small-attempt3.out', 'w')
count=0

for line in source:
	string = "Case #" + str(count) + ": "
		
	for c in line:
		if 'a' in c:
			string = string + 'y'
		if 'b' in c:
			string = string + 'h'
		if 'c' in c:
			string = string + 'e'
		if 'd' in c:
                        string = string + 's'
                if 'e' in c:
			string = string + 'o'
                if 'f' in c:
                        string = string + 'c'
                if 'g' in c:
                        string = string + 'v'
                if 'h' in c:
                        string = string + 'x'
                if 'i' in c:
                        string = string + 'd'
                if 'j' in c:
                        string = string + 'u'
                if 'k' in c:
                        string = string + 'i'
                if 'l' in c:
                        string = string + 'g'
                if 'm' in c:
                        string = string + 'l'
                if 'n' in c:
                        string = string + 'b'
                if 'o' in c:
                        string = string + 'k'
                if 'p' in c:
                        string = string + 'r'
                if 'q' in c:
                        string = string + 'z'
                if 'r' in c:
                        string = string + 't'
                if 's' in c:
                        string = string + 'n'
                if 't' in c:
                        string = string + 'w'
                if 'u' in c:
                        string = string + 'j'
                if 'v' in c:
                        string = string + 'p'
                if 'w' in c:
                        string = string + 'f'
                if 'x' in c:
                        string = string + 'm'
                if 'y' in c:
                        string = string + 'a'
                if 'z' in c:
                        string = string + 'q'
                if ' ' in c:
                        string = string + ' '
                if '\n' in c:
			string = string + '\n'

	if count <= 30 and count >= 1:
		destination.write(string)
	count = count + 1

destination.close()
source.close()
