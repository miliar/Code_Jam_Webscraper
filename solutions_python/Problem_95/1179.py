a={'a':'y','l':'g','m':'l','s':'n','e':'o','j':'u','p':'r','y':'a','c':'e','k':'i','d':'s','x':'m','v':'p','n':'b','r':'t','i':'d','b':'h','t':'w','w':'f','h':'x','f':'c','o':'k','u':'j','g':'v','q':'z','z':'q'}

f1=open('A-small-attempt0.in','r')
f2=open('lang.out','w')

b=f1.readline()
b=b.rstrip('\n')
t=1

while t<=int(b):
	s=f1.readline()
	s=s.rstrip('\n')
	u=' '
	for e in s:
		if(e==' '):
			u+=' '
			continue
		for (k,v) in a.iteritems():
			if(e==k):
				u+=v

	temp='Case #'+str(t)+':'+u+'\n'
	f2.write(temp)

	t+=1		
						
