import copy
#f = open('C-small-attempt0.in')
f = open('C-large.in')
search='welcome to code jam'
rsearch=search[::-1]
cases=int(f.readline().strip())
for case in range(0, cases):
   line = f.readline().strip()
   rline=line[::-1]
   ways=[1]*len(rline)
   newways=[1]*len(rline)
   for c in rsearch:
      wc=0
      for i in range(0,len(rline)):
         p=rline[i]
         if c==p:
            wc+=ways[i]
         newways[i]=wc
      ways=copy.deepcopy(newways)
      newways=[1]*len(rline)
   count=ways[-1]
   digits=str(count+10000)[-4:]
   print("Case #"+str(case+1)+":", digits)
   
