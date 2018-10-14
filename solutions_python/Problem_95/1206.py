ident = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd',
 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r',
 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z':
'q'}


ans = open('res.txt','w')
task = open('A-small-attempt0.in','r')

n = int(task.readline())

for i in range(n):
	s = task.readline()
	res = 'Case #' + repr(i+1)  + ': '
	for c in s:
		if c in ident:
			res += ident[c]
		else:
			res += c
	ans.writelines(res)

ans.close()
task.close()