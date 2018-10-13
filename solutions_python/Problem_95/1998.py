dic = {'a': 'y', 'b':'n', 'c':'f', 'd':'i', 'e':'c', 'f':'w', 'h':'b',
'g':'l', 'i':'k', 'j': 'u', 'k':'o', 'l':'m', 'm':'x', 'n':'s', 'o':'e',
'p':'v', 'q':'z', 'r':'p', 's':'d', 't':'r', 'u':'j', 'v':'g', 'w':'t', 
'x':'h','y':'a','z':'q'}
newdic = {' ':' '}
for x in dic.keys():
	newdic[dic[x]] = x
	
with file('A-small-attempt0.in.txt') as f:
	solution = open('solution.txt','w')
	t = int(f.readline().strip())
	for x in range(0,t):
		line = f.readline().strip()
		newline = ''
		for letter in line:
			newline+=newdic[letter] 
		solution.write('Case #%i: %s\n'%(x+1, newline))
print 'done'
