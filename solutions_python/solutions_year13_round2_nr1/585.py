from numpy import multiply, product

import math

def solve(A,N, ls):
   print "A:{0} N:{1} ls:{2}".format(A,N,sorted(ls))
   ls = sorted(ls)
   #print "Sorted ls:{0}".format(ls)
   inc = 0
   
   if A == 1:
      return N
   
   for j in range(N):

      if A > ls[j]:
         A += ls[j]
      else:
         s = int(math.floor(math.log(float(ls[j]- A)/ float(A-1) + 1 , 2))) + 1
         #print "S:{0}".format(s)
         if ( s< N - j ):
            inc += s
            A += (A-1)*(2**(s) -1) + ls[j]
            
         else:
            inc += 1
            
         #print "A:{0} Inc:{1}".format(A, inc)
         
   return inc
    
    
    
def read():
    inp = "A-small-attempt3.in"
    out = "A-small-attempt3-OUT.txt"
    f = open(inp, 'r')
    fo = open(out, 'w')
    num_lines = f.readline()
    for j in range(int(num_lines)):
        
        line1 = f.readline().replace("\n","").split(" ")
        line2 = f.readline().replace("\n","").split(" ")

        ls = [int(i) for i in line2]
        result = solve(int(line1[0]),int(line1[1]), ls)
        print "Result is: ", result
        fo.write("Case #{0}: {1}".format(j+1,result))        
        fo.write("\n")
        
read()
