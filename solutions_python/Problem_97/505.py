#v2.7.2
def Pair(n,B):
   N=n
   numDigits=len(str(n))
   Digits=[]
   while n>9:
      Digits.append(n%10)
      n=n/10
   Digits.append(n)
   Digits.reverse()
   Pairs=[]
   for i in range(1,numDigits):
      Digits.append(Digits.pop(0))
      M=ToNumber(Digits)
      if (M>N and M<=B and M not in Pairs):
         Pairs.append(M)
   return len(Pairs)
def ToNumber(n):
   s=0;
   for i in n:
      s=s*10+i
   return s
import sys
sys.stdin=open('C-small-attempt1.in')
Output=open('output.txt','w+')
for i in xrange(input()):
   a,b=raw_input().split()
   A,B=int(a),int(b)
   numPairs=0
   for j in xrange(A,B+1):
      numPairs+=Pair(j,B)
   Output.write("Case #%d: %d"%(i+1,numPairs)+"\n")
#print "Done!"
Output.close()
