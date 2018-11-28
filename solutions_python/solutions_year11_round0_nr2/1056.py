import string
def process(comb,opp,l):
 out=[l[0]]
 for x in range(1,len(l)):
  out.append(l[x])
  if len(out)>=2:
   if   out[-1]+out[-2] in comb: out=out[:-2]+[comb[out[-1]+out[-2]]]
   elif out[-2]+out[-1] in comb: out=out[:-2]+[comb[out[-2]+out[-1]]]
   if (out[-1] in opp) and (opp[out[-1]] in out[:-1]): out=[]
 out=str(out); out=string.replace(out,"'",'')
 return out

#print process({},{},['E','A'])
#print process({'QR':'I'},{},['R','R','Q','R'])
#print process({'QF':'T'},{'Q':'F', 'F':'Q'},['F','A','Q','F','D','F','Q'])
#print process({'EE':'Z'},{'Q':'E', 'E':'Q'},['Q','E','E','E','E','R','A'])
#print process({},{'Q':'W', 'W':'Q'},['Q','W'])

input=file('B-small-attempt0.in','rb+').read().split('\n'); input.reverse()
output=file('B-small-attempt0.out','wb+')
for n in range(int(input.pop())):
 line=input.pop().split(' '); line.reverse()
 combos={}; opps={}; inv=[]
 for x in range(int(line.pop())):
  combo=line.pop(); combos[combo[:2]]=combo[2]
 for x in range(int(line.pop())):
  opp=line.pop(); opps[opp[0]]=opp[1]; opps[opp[1]]=opp[0]
 line.pop()
 inv=list(line.pop())
 if '\r' in inv: inv.remove('\r')
 output.write('Case #'+str(n+1)+': '+process(combos,opps,inv)+'\n')