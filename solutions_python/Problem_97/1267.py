def is_recycled(i,j) :
  i,j=str(i),str(j)
  i=list(i)
  for k in range(len(i)):
   p=i.pop(0)
   i.append(p)
   i=''.join(i)
   if i==j :
     return 1
   i=list(i)
  return 0

if __name__=='__main__' :
 z=0
 t=input()
 for a0 in range(t):
    count=0
    s=raw_input()
    s=s.strip().split()
    a,b=s[0],s[1]
    a,b=int(a),int(b)
    for i in range(a,b+1):
      for j in range(i+1,b+1):
        if j>10*i : 
          break
        z=is_recycled(i,j)
        if z== 1:
          count=count+1
    j=a0+1
    j=str(j)
    count1=str(count)
    print 'Case #'+j+': '+count1     