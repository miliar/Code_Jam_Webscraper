file = open('A.txt','r')
f2 = open('Aout.txt','w')
T=file.readline()
T=int(T)
d={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
for i in range (0,T):
	s=''
	j= i+1
	s= 'Case #'+str(j)+': '
	line=file.readline()
	words= line.split()
	for word in words:
		for k in range(0,len(word)):
				s=s+ d[word[k]]
		s=s+' '
	f2.write(s)
	f2.write('\n')
 
			

		
	
