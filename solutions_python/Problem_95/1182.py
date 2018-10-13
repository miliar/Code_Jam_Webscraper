# Program to solve A. Speaking in Tongues

sub_dic = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 
			'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 
			'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '}
			
def decrypt(line):
	out = ""
	for char in line:
		if char != '\n':
			out += sub_dic[char]
	return out
	
filename = "sub-2.in"
infile = open(filename, 'r')

outfile = open("output.txt", 'w')

first_line = True
case = 1

for line in infile:
	if first_line:
		first_line = False
		continue
	outfile.write("Case #" + str(case) + ": "+ decrypt(line) + "\n")
	case += 1

infile.close()
outfile.close()