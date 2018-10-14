
import math

def is_palindrome(i):
  s = str(i)
  first = 0
  last = len(s)-1
  
  while last > first:
    if s[first] != s[last]:
      return False
    
    last -= 1
    first += 1
  return True

def square_generator():
  i = 1
  while(True):
    yield i*i
    i += 1
  
  
def generate_fair_squares(limit):
  s = []
  generator = square_generator()
  while(True):
    p = generator.next()
    if p > limit:
      break
    if is_palindrome(p) and is_palindrome(int(math.sqrt(p))):
      s.append(p)
  return s

def fair_square_generator():
  i = 1
  while(True):
    if is_palindrome(i):
      sq = i*i
      

def main():
  limit = int(math.sqrt(10**100)+1)
  print "#limit: ",limit
  numbers = generate_fair_squares(limit)
  print "magic_numbers=",numbers
if __name__ == "__main__":
  main()