table = {'a' : 'y',
'b' : 'h',
'c' : 'e',
'd' : 's',
'e' : 'o',
'f' : 'c',
'g' : 'v',
'h' : 'x',
'i' : 'd',
'j' : 'u',
'k' : 'i',
'l' : 'g',
'm' : 'l',
'n' : 'b',
'o' : 'k',
'p' : 'r',
'q' : 'z',
'r' : 't',
's' : 'n',
't' : 'w',
'u' : 'j',
'v' : 'p',
'w' : 'f',
'x' : 'm',
'y' : 'a',
'z' : 'q',
' ' : ' '
}
T = input();
f = open("output.put", "w")
for i in range(T):
	sent = raw_input()
	d = ["%s" % table[x] for x in sent]
	s = "".join(d)
	f.write('Case #' + str(i+1) + ': ' + s + '\n')
