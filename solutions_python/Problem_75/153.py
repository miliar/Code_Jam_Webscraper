for T in range(input()):
 x=raw_input().split();i=int(x[0]);m={};d={};h=[]
 for s in x[1:i+1]:m[s[:2]]=m[s[1::-1]]=s[2]
 for s in x[i+2:-2]:d[s]=d[s[::-1]]=1
 for c in x[-1]:
  while h and h[-1]+c in m:c=m[h.pop()+c]
  if any(a+c in d for a in h):h=[]
  else:h+=[c]
 print"Case #%s:"%(T+1),`h`.replace("'","")