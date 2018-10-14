import sys

#Mapping from googlerese to english
gtoe = {
	'y':'a',
	'q':'z',
	'e':'o',
	'j':'u',
	'p':'r',
	'm':'l',
	's':'n',
	' ':' ',
	'\n':'',
	'l':'g',
	'c':'e',
	'k':'i',
	'd':'s',
	'x':'m',
	'v':'p',
	'n':'b',
	'r':'t',
	'i':'d',
	'b':'h',
	't':'w',
	'a':'y',
	'h':'x',
	'w':'f',
	'f':'c',
	'o':'k',
	'u':'j',
	'g':'v',
	'z':'q'
	}
	
if (len(sys.argv) > 1):
	file = open(sys.argv[1],'r')
	outfile = open("output", 'w')
	cases = file.readline()
	cases = int(cases)
	iters = 0
	
	while(iters < cases):
		#Read in a test case
		input = file.readline()
		output = []
		
		#Translate every letter in that test case
		for letter in input:
			output.append(gtoe[letter])
		
		#Write out to outfile	
		output = ''.join(output)
		outfile.write("Case #" + str(iters+1) + ": " + output + '\n')
			
		iters += 1
		
	file.close()
	outfile.close()
		