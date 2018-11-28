#Magicka
from sets import Set

for case in xrange(int(raw_input())):
   inps=raw_input().split()
   c=int(inps[0])
   inps=inps[1:]
   
   combis={}
   for i in inps[:c]:
      combis[(i[0],i[1])]=i[2]
      combis[(i[1],i[0])]=i[2]
      
   #print "Combis:",combis
   
   inps=inps[c:]
   d=int(inps[0])
   inps=inps[1:]
   
   ops=[]
   for i in inps[:d]:
      ops.append([i[0],i[1]])
      ops.append([i[1],i[0]])
   
   #print "Ops:",ops
   
   inps=inps[d:]
   n=int(inps[0])
      
   li=[]
   contains={}
   for i in inps[-1]:
      #li.append(i)
      if len(li)>0 and (li[-1],i) in combis:
         contains[li[-1]]-=1
         li=li[:-1]+[combis[(li[-1],i)]]
      else:
         for j in ops:
            if j[0]==i:
               if j[1] in contains and contains[j[1]]>0: #clear list
                  li=[]
                  contains={}
                  break
         else:
            li.append(i)
            if i in contains:
               contains[i]+=1
            else:
               contains[i]=1
     #       print contains
   
   print "Case #"+str(case+1)+": ["+", ".join(li)+"]"
