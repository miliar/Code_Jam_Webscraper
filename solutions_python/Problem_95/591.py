#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
fname="googex2.in"
file=open(fname)


out=open("out_"+fname, "w")

m={
	'\n': '',
	' ': ' ',
	'y':'a'	,
	'n':'b'	,
	'f':'c'	,
	'i':'d'	,
	'c':'e'	,
	'w':'f'	,
	'l':'g'	,
	'b':'h'	,
	'k':'i'	,
	'u':'j'	,
	'o':'k'	,
	'm':'l'	,
	'x':'m'	,
	's':'n'	,
	'e':'o'	,
	'v':'p'	,
	'z':'q'	,
	'p':'r'	,
	'd':'s'	,
	'r':'t'	,
	'j':'u'	,
	'g':'v'	,
	't':'w'	,
	'h':'x'	,
	'a':'y'	,
	'q':'z'	}
	
from pprint import pprint
nbCases=int(file.readline())
for j in range(1,nbCases+1):
	line=file.readline()
	res=""
	for i in range(0,len(line)):
		res=res+m[line[i]]
	
	
	out.write("Case #"+str(j)+": "+str(res))
	print "Case #"+str(j)+": "+str(res)
	out.write("\n")
out.close()

#def m(l):
