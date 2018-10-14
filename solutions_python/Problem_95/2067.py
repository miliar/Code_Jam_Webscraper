googlerese = {
   'a': 'y',
   'b': 'h',
   'c': 'e',
   'd': 's',
   'e': 'o',
   'f': 'c',
   'g': 'v',
   'h': 'x',
   'i': 'd',
   'j': 'u',
   'k': 'i',
   'l': 'g',
   'm': 'l',
   'n': 'b',
   'o': 'k',
   'p': 'r',
   'q': 'z',
   'r': 't',
   's': 'n',
   't': 'w',
   'u': 'j',
   'v': 'p',
   'w': 'f',
   'x': 'm',
   'y': 'a',
   'z': 'q'
}

def translate (inputString):
   output = ""
   for char in inputString:
      output += googlerese.get(char, char)
   return output
      

f = open("input.txt", "r");
lines = f.readlines()
f.close()

# Get the number of lines and shorten the array
numLines = int(lines[0].strip())
lines = lines[1:]

f = open("output.txt", "w");

i = 1
for line in lines:
	f.write("Case #" + str(i) + ': ');
	f.write(translate(line))
	i += 1
	
f.close()