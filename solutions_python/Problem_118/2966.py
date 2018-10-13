from math import sqrt 
def ispalindrome(number):
   n = number
   rev=0  
   while n>0: 
    r=n%10 
    rev = rev*10 + r 
    n=n/10 
   
   if rev==number: 
      return True 
   else: 
      return False 

def fair_sq_count(start,end):
   count =0 
   for i in range(start,end+1): 
      sqr = sqrt(i) 
      if sqr != int(sqr):
         continue 
      else:
          sqr=int(sqr)
          if (ispalindrome(i)==True) and (ispalindrome(sqr)== True):
             count = count + 1 
          
   return count 


if __name__ == "__main__":
   f=open("C-small-attempt4.in")
   vals=f.readlines()
   y=int(vals[0])
   vals=vals[1:]
   cases=[a.rstrip("\n") for a in vals] 
   results=[]
   i=0 
   f1=open("result_small.txt","w")
   for case  in cases:
     
     a,b=case.split(" ") 
     a=int(a)
     b=int(b)
     count = fair_sq_count(a,b)
     s="Case #"+str(i+1)+": "+str(count)
     f1.write(s+"\n")
     i=i+1
 
