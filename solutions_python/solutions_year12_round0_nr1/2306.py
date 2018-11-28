#y>a#
#e>o#
#j>u#
#p>r#
#m>l#
#s>n#
#b>h#
#q>z#
#a>y#
#c>e#
#d>s#
#f>c#
#g>v#
#h>x#
#i>d#
#k>i#
#l>g#
#n>b#
#o>k#
#r>t#
#t>List[w]#
#u>j#
#v>p#
#List[w]>f#
#x>m#
#z>q#

Opened = open('A-small-attempt1.in', 'r')
Number = Opened.readline()
File = Opened.readlines()
Number = int(Number)
Cases = File[0:Number]
Blank = []
z = 1
for i in Cases:
	List = list(i)
	Num = len(List)
	Rag = range(Num)
	Pieces = []
	for w in Rag:
		if List[w] == 'y':
			d = 'a'
		if List[w] == 'e':
			d = 'o'
		if List[w] == 'j':
			d = 'u'
		if List[w] == 'p':
			d = 'r'
		if List[w] == 'm':
			d = 'l'
		if List[w] == 's':
			d = 'n'
		if List[w] == 'b':
			d = 'h'
		if List[w] == 'q':
			d = 'z'
		if List[w] == 'a':
			d = 'y'
		if List[w] == 'c':
			d = 'e'
		if List[w] == 'd':
			d = 's'
		if List[w] == 'f':
			d = 'c'
		if List[w] == 'g':
			d = 'v'
		if List[w] == 'h':
			d = 'x'
		if List[w] == 'i':
			d = 'd'
		if List[w] == 'k':
			d = 'i'
		if List[w] == 'l':
			d = 'g'
		if List[w] == 'n':
			d = 'b'
		if List[w] == 'o':
			d = 'k'
		if List[w] == 'r':
			d = 't'
		if List[w] == 't':
			d = 'w'
		if List[w] == 'u':
			d = 'j'
		if List[w] == 'v':
			d = 'p'
		if List[w] == 'w':
			d = 'f'
		if List[w] == 'x':
			d = 'm'
		if List[w] == 'z':
			d = 'q'
		if List[w] == ' ':
			d = ' '
		if List[w] == '\n':
			d = ''
		Pieces.append(d)
	Blank.append("".join(Pieces))
for i in Blank:
	print 'Case #'+str(z)+': '+i
	z += 1