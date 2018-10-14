import math
import codecs
def pol(num):
   
    n=str(num)
    l=len(n)
    s=""
    for i in range(1,l+1):
        s=s+n[l-i]
    if s==n:
        return True
    else:
        return False
          
def is_square(num):
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num: 
        return True
    else:
        return False

    

with open("C-small-attempt3.in") as f:
    data = f.readlines()
    cases = int(data[0])      
def fair_and_sqyare(a,b):
    count = 0
    for i in xrange(a, b + 1):
       if (pol(i) and is_square(i)):   
           if (pol(int(math.sqrt(i)))):
               count += 1
    return count


  




def main():
    
 for i in range(cases):
    a = int(data[1:][i].split(" ")[0])
    b = int(data[1:][i].split(" ")[1])

    print "Case #%s: %s" % ((i + 1),  fair_and_sqyare(a, b))
        
main()

