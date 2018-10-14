import sys

def is_palindrome(i):
  s = str(i)
  a = 0
  b = len(s) - 1
  while (a < b):
    if (s[a] != s[b]):
      return 0
    a += 1
    b -= 1
  return 1
  
def fill_fair_and_square_to(B):
  global palindromes
  global fair_and_square
  
  curr = palindromes[-1] + 1
  while (fair_and_square[-1] <= B):
    if (is_palindrome(curr)):
      palindromes.append(curr)
      sqr = curr * curr
      if (is_palindrome(sqr)):
        fair_and_square.append(sqr)
    curr += 1
    
def get_count_in_range(A, B):
  a = 0
  while (fair_and_square[a] < A):
    a += 1
    
  b = a
  while (fair_and_square[b] <= B):
    b += 1
    
  return b - a

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())
palindromes = [1]
fair_and_square = [1]

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  line = [int(v) for v in infile.readline().split()]
  A = line[0]
  B = line[1]
  
  fill_fair_and_square_to(B)
  
  print get_count_in_range(A, B)
  

infile.close()