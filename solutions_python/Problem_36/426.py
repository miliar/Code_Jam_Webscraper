def ocurr(phrase,text):
	if len(phrase)==1: return text.count(phrase[0])
	res=0
	for i in range(len(text)-len(phrase)):
		if phrase[0]==text[i]: res+=ocurr(phrase[1:],text[i:])
	return res

#print ocurr('welcome to code jam',"""So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.""")
#print ocurr('ab','aaaaaaaaaabbbbbbbbbb')

f=open('C-small-attempt0.in','r')
out=""
for case in range(int(f.readline())):
	out+="Case #"+str(case+1)+": "+str(ocurr('welcome to code jam',f.readline()))[-4:].zfill(4)+"\n"
outf=open('C-small-attempt0.out','w')
outf.write(out)
