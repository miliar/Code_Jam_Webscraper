def translateStr(a):
	l=len(a)
	i=0
	result=''
	D={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
	while(i < l):
		if a[i] != ' ':
			result+=D[a[i]] 
			i+=1
		else:
			result+=' '
			i+=1
	return result

N=input()
for case in range(1,N+1):
	print "Case #"+str(case)+": "+translateStr(raw_input())
