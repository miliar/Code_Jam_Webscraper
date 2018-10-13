from math import sqrt, ceil, floor
from sys import argv
from lib.File import FileParser

def palindrome(argi):
  args = str(argi)
  return args == args[::-1]

def case_logic(case_args):
  a, b = map(int, case_args[0].split())
  base_a = int(ceil(sqrt(a)))
  base_b = int(floor(sqrt(b)))
  found = 0
  for i in range(base_a, base_b+1):
    if palindrome(i) and palindrome(i * i):
      found += 1
  return str(found)

def main(args):
  parser = FileParser(1, 1, args[0])
  problem = parser.parse_problem()
  problem.set_case_logic(case_logic)
  problem.solve()
  problem.done()

if __name__ == "__main__":
  main(argv[1:])
