#Speaking with tongues

import sys
import fileinput

mapping = {'y':'a',
			'n':'b',
			'f':'c',
			'i':'d',
			'c':'e',
			'w':'f',
			'l':'g',
			'b':'h',
			'k':'i',
			'u':'j',
			'o':'k',
			'm':'l',
			'x':'m',
			's':'n',
			'e':'o',
			'v':'p',
			'z':'q',
			'p':'r',
			'd':'s',
			'r':'t',
			'j':'u',
			'g':'v',
			't':'w',
			'h':'x',
			'a':'y',
			'q':'z',
			' ': ' ',
			'\n':'\n'}

def convert(string):
	r = ''
	for char in string:
		r = r + mapping[char]
	return r
	
def solve():
	#output file
	out = open('output','w') 
	

	#input file
	filein = fileinput.input()
	#set up test cases
	testInt = 1
	totalTests = 0
	
	#process
	for lines in filein:
		print lines
		if filein.isfirstline():
			totalTests = int(lines)
			print 'test: ' + str(totalTests)
		else:
			c = ""
			#convert
			c = convert(lines)
			print c
			#write out
			out.write('Case #' + str(testInt) + ': ' + c)
			testInt += 1
	

solve()