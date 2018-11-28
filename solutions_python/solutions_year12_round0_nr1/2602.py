#string defcode
#arg string string to be converted
#arg key dictionary holding decoder
def decode(string,key):
	donestring = ''
	for letter in string:
		if letter in key.keys():
			donestring+=key[letter]
		else:
			donestring+=letter
	return donestring

def main():
	#read in line of text
	#turn letters into other letters, ignore spaces
	#output new and improved lines
	
	key = {
			'y':'a',
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
		}
	
	file = open('A-small-attempt0.in.txt')	#open the file

	size = (int)(file.readline().split()[0])
	#print size,
	for i in range(0,size):
		s = decode(file.readline(),key)
		print "Case #"+str(i+1)+": "+s,

main()