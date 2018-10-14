s = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''
t = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
'''

ma  = {}
for i in range(0,len(s)):
	ma[s[i]] = t[i]
ma['q']='z'
ma['z']='q'
filein = open(r"d:\in.txt")

all_text = 	filein.read()
lines = all_text.split('\n')
n = int(lines[0])
out = ''
for i in range(1,n+1):
	tnew = ''
	for c in lines[i]:
		tnew += ma[c]
	out += "Case #%d: %s\n"%(i,tnew)
fileout = open(r"d:\out.txt","w")
fileout.write(out)
fileout.close()
