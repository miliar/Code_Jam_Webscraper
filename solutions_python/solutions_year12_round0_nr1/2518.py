infile = open("A-small-attempt1.in.txt")
outfile = open("output.txt", "w")

dict = {'y':'a',
	'n':'b',
	'f':'c',
	'i':'d',
	'c':'e',
	'w':'f', 
	'l':'g',
	'b':'h',
	'k':'i',
	'u':'j',
	'e':'o',
	'm':'l',
	'x':'m',
	's':'n',
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
	'o':'k',
	' ':' ',
	'\n':'',
		}

case = 1
caseNum = int(infile.readline())

while 1:
	line = list(infile.readline())
	if not line:
		break

	char = ""
	for j in range(len(line)):
		char += dict[line[j]]

	strCase = str(case)
	outfile.write('Case #'+ strCase + ': ' + char + '\n')
	case += 1


outfile.close()
infile.close()





