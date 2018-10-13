import string
G2P ={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
f = file('small.input','r')
inp = f.readline()
out = file('small.out','w')
i =0
for j in range(int(inp)):
	words = f.readline().split()
	actual = []
	casenum = j
	for word in words:
		newword=''
		while i < len(word):
			newword=newword+G2P[word[i]]
			i+=1
		actual.append(newword)
		i=0
	out.write('Case #'+str(casenum+1)+': '+string.join(actual)+'\n')
	actual=[]
	





