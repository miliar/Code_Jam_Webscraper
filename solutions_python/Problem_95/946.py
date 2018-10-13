d = {'a':'y', 'b':'h' , 'c':'e', 'd':'s', 'e':'o' , 'f':'c', \
'g':'v', 'h':'x' , 'i':'d', 'j':'u', 'k':'i' , 'l':'g', 'm':'l', \
 'n':'b' , 'o':'k', 'p':'r', 'q':'z' , 'r':'t', 's':'n', 't':'w' , \
 'u':'j', 'v':'p', 'w':'f' , 'x':'m', 'y':'a', 'z':'q'}
	
	
	
def func(string, num):
	newstr = ""
	for char in string:
		if char==' ':
			newstr+=' '
		else:
			newstr+=d[char]
	print "Case #" + str(num+1) + ": " + newstr
		
		
T = raw_input()
inp = []
for i in range(int(T)):
	inp.append(raw_input())
	
for j in range(len(inp)):
	func(inp[j], j)

map = dict
