import sys

f = open('A-small-attempt0.in', 'r')
out = open('output.txt', 'w')
testCases = int(f.readline())
count = 0

lettermap = { 'y':'a',
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
			  'd':'s',
			  'p':'r',
			  'z':'q',
			  'r':'t',
			  'j':'u',
			  'g':'v',
			  't':'w',
			  'h':'x',
			  'a':'y',
			  'q':'z'
			}

while (count < testCases):
	input = list(f.readline())
	output = 'Case #' + (str)(count+1) + ": "
	for char in input:
		if char != ' ' and char != '\n':
			output += lettermap[char]
		else:
			output += ' '
	output += '\n'
	out.write(output)
	count += 1

f.close()
out.close()