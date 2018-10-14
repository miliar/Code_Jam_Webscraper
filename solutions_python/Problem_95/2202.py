def replace_all(text, dic):
	t = ""
	for i in text:
		t=t+dic[i]
	return t
	
rev_googlereese = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' '}
t = int(raw_input())
i = 1
while i<=t:
	text = raw_input()
	print "Case #%d: %s" %(i,replace_all(text,rev_googlereese))
	i += 1

