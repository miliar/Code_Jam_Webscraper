n=str()
def check(n):
   l=list()
   for d in str(n):
    l.append(d)
   if sorted(l) == l:
      return 1
   else:
      return 0

t=input()
j=0
while j != t :
   j+=1
   x=input()
   x1=str(x)
   l=x1.__len__()
   z=10
   while x != 0:
      if check(x) == 1:
         print("Case #%s: %s"%(j,x))
         break
      else:
         y=(x%z)+1
         x=x-y
         z=z*10
