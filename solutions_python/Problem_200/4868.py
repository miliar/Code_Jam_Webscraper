
def next_number(n, dig):
  #mask(last_dig)
  #print(dig)
  """
  m = 10**(dig - 1)
  print('---')
  print(n)
  n /= m 
  n = int(n )
  print(n)
  n *= m  
  print(n)
  """
  n = n-1
  
  #print(n)
  #then minus 1
  return n

def tidy_check(n):
  #print(n)
  last_digit = 0
  while True:
    #last_digit = 1
    a = n%10
    n = int(n/10)
    b = n%10
    last_digit += 1
    #print(n)
    if a < b: 
      return False, last_digit
    if n == 0:
      #print(last_digit)
      break 

  return True, last_digit
  #return False

def tidy_helper(n):
  #print(n)
  while True:
    #print(n)
    flag, digit = tidy_check(n)  
    if flag == True:
      return n
    #else:
    n = next_number(n, digit)
    #print(n)
      #tidy_check( n )
  return -1 



#print(tidy_helper(1000))


t = int(input())  # read a line with a single integer
for i in range(1, t+1):
  n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case 
  res = tidy_helper(n[0])
  print("Case #{}: {} ".format(i, res))
#for it in 
  


