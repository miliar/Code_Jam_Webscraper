IN_FILE = 'A-small-attempt0.in.txt'
OUT_FILE = 'A-small.out.txt'


keymap = {  'a': 'y',
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
	    'z': 'q',
	    ' ': ' ',
	    '\n': ''	}
 


fin = open(IN_FILE)
fout = open(OUT_FILE, 'w')


N = fin.readline()

 
for n in range(int(N)):
   
   w = fin.readline()
   output = ''

   for c in range(len(w)):

      d = keymap[w[c]]      
      output = output + d
   
   fout.write('Case #' + str(n + 1) + ': ' + output + '\n')


fin.close()
fout.close()


