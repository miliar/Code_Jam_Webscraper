# Mapping:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ' '
# Y H E S O C V X D U I G L B K R Z T N W J P F M A Q ' '

googlerese = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o',
			  'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u',
			  'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k',
			  'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w',
			  'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a',
			  'z': 'q', ' ': ' ', '\n': ''}

filein = open('A-small-attempt0.in')
fileout = open('output.txt', 'w')

line_no = 0

for line in filein:
	line_no += 1
	
	if not line_no == 1:
		output = ""
		for char in line:
			output += googlerese[char]
		
		
		fileout.write("Case #%d: %s\n" % (line_no - 1, output))

filein.close()
fileout.close()		


