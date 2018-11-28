input = open('A.in')
output = open ('A.out','w')

T=int((input.readline()).rstrip())
dict={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

for i in range(0,T):
	es=''
	gs=(input.readline()).rstrip()
	for j in range(0,len(gs)):
		if (dict.has_key(gs[j])):
			es+=dict[gs[j]]
		else:
			es+=gs[j]
	output.write('Case #%d: '%(i+1))
	output.write(es+'\n')
	
