import math

INPUT_FILE = "test_input.in"

class Found(Exception):
  pass

def algo(bounds, n_case):
  lower = int(bounds[0])
  upper = int(bounds[1])
  c = 0
  for i in range(lower, upper+1):
    if math.sqrt(i)/float(1) % 1 == 0 and str(i)[::-1] == str(i) and str(int(math.sqrt(i)))[::-1] == str(int(math.sqrt(i))):
      c += 1
  print "Case #" + str(n_case) + ": " + str(c)
    


def get_cases(case_file):
  n_cases = int(case_file.readline())
  for i in range(n_cases):
    bounds = list(case_file.readline().strip().split(' '))
    algo(bounds, i+1)

def main():
  case_file = open(INPUT_FILE,'r')
  cases = get_cases(case_file)

if __name__ == '__main__':
  main()