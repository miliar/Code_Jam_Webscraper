import math
def reverse(texto):
    return texto[::-1]
    
if(__name__ == '__main__'):
  
  n_cases = int(raw_input())
  n_max = 32
  n_max2 = 10^7
  n_max3 = 10^50
  
  for case in range(n_cases):
    A = raw_input()
    A = A.split(' ')
    B = int(A[1])
    A = int(A[0])
    count = 0
          
    for i in range(int(math.sqrt(A)), int(math.sqrt(B))+1):
      word = str(i)
      if( word == reverse(word)):
	n = int(word)
	n_square = str(n*n)
	if(int(n_square) >= A and int(n_square) <= B):
	    if(n_square == reverse(n_square)):
	      count = count + 1
	
    print "Case #"+ str(case+ 1)+ ": "+ str(count)


	
  
  