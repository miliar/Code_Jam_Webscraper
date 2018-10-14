from lcj import*
with openw() as g:
 def f(l):
  s,n=l.split(' ')
  s,n=[*s],int(n)
  o=0
  while '-' in s:
   o+=1
   i=s.index('-')
   if i > len(s)-n:
    break
   s[i:i+n]=map(lambda x:'+'if x=='-'else '-',s[i:i+n])
  return o if not'-'in s else 'IMPOSSIBLE'
 for l in lines('A'):
  case(g,f(l))