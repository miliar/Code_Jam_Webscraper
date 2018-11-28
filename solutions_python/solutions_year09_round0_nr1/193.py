import copy 

casenum=1
#f=open('test.txt')
#f=open('A-small-attempt0.in')
f=open('A-large.in')
lines=f.readlines()
#wc=int(lines[0].split()[0])
wc=int(lines[0].split()[1])
tc=int(lines[0].split()[2])
words=[]
for l in lines[1:wc+1]:
   words.append(l.strip())
for l in lines[wc+1:]:
   ts=[]
   w=""
   inp=False
   for c in l.strip()+')':
      if c=='(':
         inp=True
      else:
         if c != ')':
            if not inp:
               ts.append(c)
            else:
               w=w+c
         elif w!="":
            ts.append(w)
            w=""
            inp=False
   inds=[]
   for i in range(0, len(ts)):
      inds.append( (i, ts[i]) )
   inds.sort(key=lambda x: len(x[1]))
   iwords = copy.deepcopy(words)
   iwords2=[]
   #print(inds)
   for e in inds:
      for w in iwords:
         if w[e[0]] in e[1]:
            iwords2.append(w)
      iwords, iwords2 = iwords2, []
      #print(iwords)
   #print(iwords)
   print("Case #"+str(casenum)+":", len(iwords))
   casenum+=1
   
