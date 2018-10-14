import math
def is_palindrome(num):
  name = str(num)
  return name == name[::-1]

def num_fair_square(bottom, top):
  total = 0
  low = int(math.ceil(math.sqrt(bottom)))
  high = int(math.floor(math.sqrt(top)))
  for x in range(low, high+1):
    if (is_palindrome(x) and is_palindrome(x*x)):
      #print x
      total += 1
  return total

if __name__ == '__main__':
  #file read
  f = open('/home/jfrantz/jam2013/test.txt')
  lines = f.readlines()
  for i in range(1, int(lines[0]) + 1):
    this = [int(s) for s in lines[i].split() if s.isdigit()]
    print("Case #"+str(i)+": "+str(num_fair_square(this[0], this[1])))
