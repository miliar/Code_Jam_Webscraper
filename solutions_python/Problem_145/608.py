import math

def gcd(a,b):
 while b!=0: a,b=b,a%b
 return a

def powof2(n):
 while n!=1:
  if n%2==1: return False
  else: n/=2
 return True

def sol(a,b):
 k=gcd(a,b); a/=k; b/=k
 if not powof2(b): return 'impossible'
 else: return str(int(math.ceil(math.log(b/float(a),2))))

infile=file('A-small-attempt0.in','rb+'); outfile=file('A-small-attempt0.out','wb+')
for casen in range(1,int(infile.readline().strip())+1):
 outfile.write('Case #%i: %s\r\n'%(casen,sol(*[int(x) for x in infile.readline().strip().split('/')])))