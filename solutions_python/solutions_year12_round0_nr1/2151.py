d = dict(a='y',b='h',c='e',d='s',e='o',f='c',g='v',h='x',i='d',j='u',k='i',l='g',
		m='l',n='b',o='k',p='r',q='z',r='t',s='n',t='w',u='j',v='p',
		w='f', x='m',y='a',z='q')
d[' '] = ' '
d['\n'] = '\n'

file = open('tongues.in')
N = int(file.readline())

print N

i = 1
for line in file:
	if line == '' or line == '\n': break
	newline = 'Case #' + str(i) + ": "
	for ch in line:
		newline += d[ch]
	print newline,
	i = i + 1

print
