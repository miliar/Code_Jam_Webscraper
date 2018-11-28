mymap={
'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q',
' ':' ',
'\n':'\n',
'\t':'\t',
'\r':'\r'
}
def conv(grese):
	final=""
	for j in range(0,len(grese)):
		final=final+mymap[grese[j]]
	return final
in_f=open('A-small-attempt1.in','r')
out_f=open('out','w')
tests=in_f.readline()
while tests!='':
	for i in range(0,int(tests)):
		grese=in_f.readline()
		eng=conv(grese)
		out_f.write("Case #"+str(i+1)+": "+str(eng))
	tests=in_f.readline()
in_f.close()
out_f.close()
