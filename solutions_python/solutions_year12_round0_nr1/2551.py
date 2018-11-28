import sys

i = int(raw_input())
mapping={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

for j in range(0,i):
	str= raw_input()
	print "Case #",
	sys.stdout.softspace=False
	print j+1,
	sys.stdout.softspace=False
	print ":",
	for x in range(0,len(str)):
		if (str[x] ==' '):
			print " ",
			sys.stdout.softspace=False
		else:
			print mapping[str[x]],
			sys.stdout.softspace=False
	print	
