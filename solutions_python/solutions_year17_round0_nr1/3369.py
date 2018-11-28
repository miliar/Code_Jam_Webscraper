t=int(input())
for z in range(t):
  s,k=[str(s) for s in input().split(" ")]
  k=int(k)
  isf=True
  f=0
  for a in range(len(s)-k+1):
      i=0
      for b in s[:-(k-1)]:
        i+=1
        if b =='+':
          isf=False
          continue
        else:
          isf=True
          break
        isf=False
      if isf:
        f+=1
        temp=''
        for c in s[i-1:i+k-1]:
          if c=='+':  
            temp=temp+'-'
          else:
            temp=temp+'+'
        s=s[:i-1]+temp+s[i+k-1:]
      else:
        break
  ish=True
  for d in s:
    if d=='+':
      ish=True
      continue
    else:
      ish=False
      print("Case #{}: {}".format(z+1,"IMPOSSIBLE"))
      break
  if ish:
    print("Case #{}: {}".format(z+1,f)) 
  
    
  
