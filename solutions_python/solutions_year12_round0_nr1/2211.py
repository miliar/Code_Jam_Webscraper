InpFile=open('SITInput.txt')
OutFile=open('SITOutput.txt','w')
dict={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' '}
n=int(InpFile.readline().strip())
k=1
while(k<=n):
	line=InpFile.readline().strip()
	l=len(line)
	OutFile.write('Case #%d: '%(k))
	for i in range(l):
		OutFile.write('%s'%(dict[line[i]]))		
	OutFile.write('\n')
	k=k+1
InpFile.close()
OutFile.close()