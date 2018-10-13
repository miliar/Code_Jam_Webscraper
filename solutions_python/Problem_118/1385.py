import math
fname=raw_input("input filename:")
data=open(fname,"rev+")
text=data.readlines()
data.close()
nos=int(text[0])
nos=nos
tn=1

def perfect(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def reverse_int(num):
    rev=0
    while(num>0):
     dig=num%10
     rev=rev*10+dig
     num=num/10
    return rev
 
def fun(A,B,c):
    count=0
    for x in xrange(A,B+1):
      if perfect(x):
       h=reverse_int(x)
       if h==x:
         z=int(math.sqrt(h))
         q=reverse_int(z)
         if q==z:
          count+=1
    value=count
    out=open("result.txt","a+")
    out.writelines("Case #%d: %d \n" %(c,value))     
    out.close()
   
for x in range(0,nos):
    ln=text[x+1]
    ln=ln.strip()
    ln1=ln.split()
    A=int(ln1[0])
    B=int(ln1[1])
    fun(A,B,x+1)
    

