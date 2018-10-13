#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# author Ladislav Vrbsky
# Google Code Jam 2017
# Qualification round
# Problem B. Tidy Numbers

def last_tidy(n):
  order = 0

  while 10**(order-1) < n:
    if is_tidy(n):
      return n
    rest = n % 10**(order)
    digit = n//10**order % 10
    #substract to create digit 9 at current position
    # print((digit+1)*(10**order))
    n -= (digit+1)*(10**order)
    order += 1

  return -1

def is_tidy(n):
  order = 0
  last_digit = 10
  while 10**(order-1) < n:
    digit = n//10**order % 10
    # print(last_digit, digit)
    if last_digit >= digit:
      last_digit = digit
    else:
      # print(False)
      return False
    order += 1
  # print(True)
  return True


def main():
  # is_tidy(10000)
  # is_tidy(1110)
  # is_tidy(349999)
  # is_tidy(11)
  # is_tidy(98)
  # is_tidy(5)
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, last_tidy(n)))

if __name__ == '__main__':
  main()