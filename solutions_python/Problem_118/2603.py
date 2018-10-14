f = open('C-small-attempt0.in', 'r')
g = open('output.txt','wb')
string=f.read()
f.close()
strList=string.split("\n")
for i in xrange(int(strList[0])):
	n=0
	a=strList[i+1].split(" ")
	print a
	for j in xrange(int(a[1])-int(a[0])+1):
		if str(j+int(a[0]))==str(j+int(a[0]))[::-1]:
			if str(int((j+int(a[0]))**.5))==str(int((j+int(a[0]))**.5))[::-1]:
				if (j+int(a[0]))**.5==int((j+int(a[0]))**.5):	
					print j+int(a[0])
					n+=1
					
	g.write("Case #"+str(i+1)+": "+str(n)+"\n")
g.close()
z=input()