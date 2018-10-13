import sys


d = {
'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q'
}

# get command line arguments
if len(sys.argv) != 2:
        print 'Usage: '+sys.argv[0]+' input'
        sys.exit(-1)

# read input file
f = open(sys.argv[1],'r')
lines = f.readlines()
num_test_case = int(lines[0])

for i in range(num_test_case):
	line = lines[i+1]
	new_line = ''
	for c in line:
		if c in d.keys():
			new_line += d[c]
		else:
			new_line += ' '
	print 'Case #'+str(i+1)+': '+new_line.strip()
