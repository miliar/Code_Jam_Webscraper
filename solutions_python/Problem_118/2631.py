
import sys
from math import sqrt


def is_sq(num):
  root = sqrt(num)
  if ((int(root + 0.5))**2) == num:
    return int(root + 0.5)
  else:
    return False

def is_pali(num):
  number_string = list(str(num))
  for i in range(0,len(number_string)/2):
    if number_string[i] != number_string[len(number_string)-1-i]:
      return False
  return True

def num_fair_and_sq(low,up):
  count = 0
  for number in range(low, up):
    if is_pali(number):
      sqrt = is_sq(number)
      if sqrt:
        if is_pali(sqrt):
          count += 1
  return count

def parse():
  file_input = sys.stdin.readlines()

  cases = eval(file_input.pop(0))

  for case in range(0,cases):
    interval = map(lambda x: eval(x),file_input[case].strip().split())
    lower, upper = interval[0], interval[1]
    print "Case #{0}: {1}".format(case+1,num_fair_and_sq(lower,upper+1))



def main():
  parse()

if __name__ == '__main__':
  main()
