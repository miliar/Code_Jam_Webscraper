# C:\Python27\

from sys import argv

script, filename = argv

dict = {

	'a' : 'y',
	'b' : 'h',
	'c' : 'e',
	'd' : 's',
	'e' : 'o',
	'f' : 'c',
	'g' : 'v',
	'h' : 'x',
	'i' : 'd',
	'j' : 'u',
	'k' : 'i',
	'l' : 'g',
	'm' : 'l',
	'n' : 'b',
	'o' : 'k',
	'p' : 'r',
	'q' : 'z',
	'r' : 't',
	's' : 'n',
	't' : 'w',
	'u' : 'j',
	'v' : 'p',
	'w' : 'f',
	'x' : 'm',
	'y' : 'a',
	'z' : 'q',
	' ' : ' '

}

txt = open(filename)
output = open("output.txt", 'w')

a = 1
b = 1
for line in txt:
	if a is 1:
		a = 2
		continue
	output.write("Case #")
	output.write(str(b))
	output.write(": ")

	for x in line:
		
		if x == "\n":
			output.write("\n")
		else:
			output.write(dict[x])
	b = b + 1