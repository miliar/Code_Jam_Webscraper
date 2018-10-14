jamd={'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
def abc():
	test=0
	test=input()
	j=0
	while j < test:
		j=j+1
		strval=raw_input()
		nval="Case #"
		nval=nval+str(j)+": "
		for i in range(0,len(strval)):
			if(strval[i]!=' '):
				nval=nval+jamd[strval[i]]
			else:
				nval=nval+' '
		print nval
		
		
	
abc()