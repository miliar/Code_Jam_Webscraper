import math
import sys
inputFilePath 	= sys.argv[1]
outputFilePath 	= sys.argv[2]

def isPalindrome(word):
    return word == ''.join(reversed(word))
  
def isFairAndSquare(x) :
  if isPalindrome(str(x)) :
    sqrt_float	= math.sqrt(x)
    sqrt_int	= int(sqrt_float)
    if sqrt_float == sqrt_int :
      return isPalindrome(str(sqrt_int))
    return False
  else :
    return False
  
def main() :   
  with open(inputFilePath) as fIn :
    with open(outputFilePath,'wb') as fOut :
      T	= int(fIn.next().strip())
      for t in xrange(T) :
	A,B	= map(int,fIn.next().strip().split())
	res	= len([ x for x in xrange(A,B+1) if isFairAndSquare(x)])
	fOut.write('Case #%i: %i\n' % ((t+1),res))

if __name__ == '__main__' :
  main()