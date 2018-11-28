import sys
import string
import re

if len(sys.argv) < 2:
	print 'You should give the filename of the input file as an argument!'
else:
	filename=sys.argv[1]
	
	file=open(filename)
	
	firstline=string.split(file.readline(), ' ')
	
	words=[]
	tokens=[]
	matches=[]
	
	for i in range(0, int(firstline[1])):
		words.append(file.readline())
	
	for i in range(0, int(firstline[2])):
		tokens.append(file.readline())
	
	file.close()
		
	for t in tokens:
		t=t.replace('(', '[')
		t=t.replace(')', ']')

		reg=re.compile(t)
		count=0
		
		for w in words:
			if reg.match(w):
				count=count+1
		
		matches.append(count)
		
	out = open('output_'+filename, 'w')
	
	for i in range(0, int(firstline[2])):
		out.write('Case #'+str(i+1)+': '+str(matches[i])+'\n')
		
	out.close()