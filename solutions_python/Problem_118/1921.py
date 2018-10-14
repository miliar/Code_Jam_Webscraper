# fair and square
def isrev(x):
   rev=0
   n=x
   while x>0 :
      t=x%10
      #if (t>3) : return 0
      rev*=10
      rev+=t
      x/=10
   if rev==n: return 1
   else: return 0
y=10**14
x=0
while x<y :
   if isrev(x)==1 and isrev(x*x)==1:
      print x,"=>",x*x
   x+=1    
