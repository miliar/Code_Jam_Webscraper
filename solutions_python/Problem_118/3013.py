import math
def palindrome(n):
     n=int(n)
     rev_n=int(str(n)[::-1])
     if n==rev_n:
         return True
     else:
          return False


def isSquare(n):
     tst =int(math.sqrt(n) + 0.5)
     return tst*tst == n
 
           

a=[]
f=open("input.txt","r")
n = f.readline()
line=f.readline()
case=0

while line:
     count=0
     case=case+1
     a=line.split()
     A=int(a[0])
     B=int(a[1])

     for i in range(A,B+1):
          if palindrome(i):
               
               if isSquare(i):
                    if palindrome(math.sqrt(i)):
                         
                         count=count+1

     print 'Case #%d: %d' %(case,count)
               
     






    
     line = f.readline()
f.close()
