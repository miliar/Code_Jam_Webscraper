a=input()
for i in range(0,int(a)):
  s=raw_input()
  b=s.split(" ")
  l=list(b[0])
  c=int(b[1])
  length=len(l)
  count=0
  for j in range(0,length-c+1):
    if(l[j]=='-'):
      count+=1
      for u in range(int(c)):
        if(l[j+u]=='+'):
          l[j+u]='-'
        else:
          l[j+u]='+'
  if("-" in l):
    print("Case #%d: %s"%(i+1,"IMPOSSIBLE")) 
  else:     
    print("Case #%d: %d"%(i+1,count))
