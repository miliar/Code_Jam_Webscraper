maps = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u','k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '}
t = int(input())
t_unchanged = t
while(t>0):
	t = t - 1
	sent = str(raw_input())
	sent = list(sent)
	for i in range(len(sent)):
		change = sent[i]
		change = maps[change]
		sent[i] = change
	sent = ''.join(sent)
	print "Case #"+str(t_unchanged-t)+":",
	print sent
