quarternions =  \
{				\
'+11': '+1',	\
'+1i': '+i',	\
'+1j': '+j',	\
'+1k': '+k',	\
'+i1': '+i', 	\
'+ii': '-1', 	\
'+ij': '+k', 	\
'+ik': '-j', 	\
'+j1': '+j', 	\
'+ji': '-k', 	\
'+jj': '-1', 	\
'+jk': '+i', 	\
'+k1': '+k', 	\
'+ki': '+j', 	\
'+kj': '-i', 	\
'+kk': '-1', 	\
'-11': '-1',	\
'-1i': '-i',	\
'-1j': '-j',	\
'-1k': '-k',	\
'-i1': '-i', 	\
'-ii': '+1', 	\
'-ij': '-k', 	\
'-ik': '+j', 	\
'-j1': '-j', 	\
'-ji': '+k', 	\
'-jj': '+1', 	\
'-jk': '-i', 	\
'-k1': '-k', 	\
'-ki': '-j', 	\
'-kj': '+i', 	\
'-kk': '+1', 	\
}


def found_K(characters):
	char_K = '+' + characters[0]
	characters = characters[1:]

	#print characters
	for next_char in characters:
		char_K = quarternions[(char_K + next_char)]

	if char_K == '+k':
		return True
	else:
		return False


def found_JK(characters):
	char_J = '+' + characters[0]
	characters = characters[1:]
	solved = False

	#print characters
	for pos, next_char in enumerate(characters):
		if char_J == '+j':
			if found_K(characters[(pos):]):
				solved = True
				break
			else:
				break
		else:
			char_J = quarternions[(char_J + next_char)]

	return solved


if __name__ == '__main__':
	T = int(raw_input())

	for i in xrange(0, T):
		input_line = raw_input().split()
		L = int(input_line[0])
		X = int(input_line[1])

		characters = raw_input()*X

		if len(characters) < 3:
			print "Case #%d: NO" %(i+1)
		elif L < 2:
			print "Case #%d: NO" %(i+1)
		else:
			char_I = '+' + characters[0]
			characters = characters[1:]
			solved = 'NO'
			
			#print characters
			for pos, next_char in enumerate(characters):
				if char_I == '+i':
					if found_JK(characters[(pos):]):
						solved = 'YES'
						break
					else:
						break
				else:
					char_I = quarternions[(char_I + next_char)]

			print "Case #%d: %s" %(i+1, solved)



