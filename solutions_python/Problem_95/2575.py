f=open("input", 'r')

a=[]
code=""
codes=[]
fread=f.readlines()

for item in fread[1:]:
	code=''
	length=len(item)
	for i in range(length):
		if item[i]=='y':
			code=code+'a'
			
		elif item[i]=='n':
			code=code+'b'
			
		elif item[i]=='f':
			code=code+'c'
			
		elif item[i]=='i':
			code=code+'d'
			
		elif item[i]=='c':
			code=code+'e'
			
		elif item[i]=='w':
			code=code+'f'
			
		elif item[i]=='l':
			code=code+'g'
			
		elif item[i]=='b':
			code=code+'h'
			
		elif item[i]=='k':
			code=code+'i'
			
		elif item[i]=='u':
			code=code+'j'
			
		elif item[i]=='o':
			code=code+'k'
			
		elif item[i]=='m':
			code=code+'l'
			
		elif item[i]=='x':
			code=code+'m'
			
		elif item[i]=='s':
			code=code+'n'
		
		elif item[i]=='e':
			code=code+'o'
			
		elif item[i]=='v':
			code=code+'p'
			
		elif item[i]=='z':
			code=code+'q'
			
		elif item[i]=='p':
			code=code+'r'
			
		elif item[i]=='d':
			code=code+'s'
			
		elif item[i]=='r':
			code=code+'t'
			
		elif item[i]=='j':
			code=code+'u'
			
		elif item[i]=='g':
			code=code+'v'
			
		elif item[i]=='t':
			code=code+'w'
			
		elif item[i]=='h':
			code=code+'x'
			
		elif item[i]=='a':
			code=code+'y'
			
		elif item[i]=='q':
			code=code+'z'
		elif item[i]==' ':
			code=code+' '
			
	codes.append(code)
m=0
for text in codes:
	m=m+1
	format="Case #%d: %s"%(m,text)
	print format
		
