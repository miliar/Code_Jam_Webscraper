def decode (s, i):
        nl = ''
	for word in s:
	        nw = ''
		for letter in word:
                	x = f(letter)
                        nw = nw + x 
                nl = nl + nw
        print "Case #%d: %s" %(i+1, nl)


def f(letter):
	if letter is 'a': return 'y'
        elif letter is 'b': return 'h'
        elif letter is 'c': return 'e'
        elif letter is 'd': return 's'
        elif letter is 'e': return 'o'
        elif letter is 'f': return 'c'
        elif letter is 'g': return 'v'
        elif letter is 'h': return 'x'
        elif letter is 'i': return 'd'
        elif letter is 'j': return 'u'
        elif letter is 'k': return 'i'
        elif letter is 'l': return 'g'
	elif letter is 'm': return 'l'
	elif letter is 'n': return 'b'
	elif letter is 'o': return 'k'
	elif letter is 'p': return 'r'
	elif letter is 'q': return 'z'
	elif letter is 'r': return 't'
	elif letter is 's': return 'n'
	elif letter is 't': return 'w'
	elif letter is 'u': return 'j'
	elif letter is 'v': return 'p'
	elif letter is 'w': return 'f'
	elif letter is 'x': return 'm'
	elif letter is 'y': return 'a'
	elif letter is 'z': return 'q'
        elif letter is ' ': return ' '
#        elif letter is '\n': return '\n'



T = int(raw_input())

for i in range(T):
	s = raw_input ()
	decode (s, i)

