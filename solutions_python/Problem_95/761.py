def subs(c):
	if c=='a':
		return 'y'
	if c=='b':
		return 'h'
	if c=='c':
		return 'e'
	if c=='d':
		return 's'
	if c=='e':
		return 'o'
	if c=='f':
		return 'c'
	if c=='g':
		return 'v'
	if c=='h':
		return 'x'
	if c=='i':
		return 'd'
	if c=='j':
		return 'u'
	if c=='k':
		return 'i'
	if c=='l':
		return 'g'
	if c=='m':
		return 'l'
	if c=='n':
		return 'b'
	if c=='o':
		return 'k'
	if c=='p':
		return 'r'
	if c=='q':
		return 'z'
	if c=='r':
		return 't'
	if c=='s':
		return 'n'
	if c=='t':
		return 'w'
	if c=='u':
		return 'j'
	if c=='v':
		return 'p'
	if c=='w':
		return 'f'
	if c=='x':
		return 'm'
	if c=='y':
		return 'a'
	if c=='z':
		return 'q'
																										

n = input()
for i in range(n):
	line = raw_input()
	words = line.split()

	words2 = []
	print("Case #"+str(i+1)+":"),
	for w in words:
		w2 = ''
		for c in w:
			w2 += subs(c)
		words2.append(w2)
	print( " ".join(words2) )








