from bisect import bisect_left, bisect_right
from math import sqrt, ceil, floor
from sys import argv
from lib.File import FileParser

precomputed = []
bottom = None
top = None

def palindrome(argi):
  args = str(argi)
  return args == args[::-1]

def case_logic(case_args):
  global precomputed
  global bottom
  global top
  a, b = map(int, case_args[0].split())
  if (not bottom) or (a < bottom) or (not top) or (b > top):
    base_a = int(ceil(sqrt(a)))
    base_b = int(floor(sqrt(b)))
    for i in range(base_a, base_b+1):
      sq = i * i
      if ((i * i) not in precomputed) and palindrome(i) and palindrome(sq):
        index = bisect_left(precomputed, sq)
        precomputed[index:index] = [sq]
    bottom = min(bottom, a)
    top = max(top, b)
  lowindex = bisect_left(precomputed, a)
  highindex = bisect_right(precomputed, b)
  return str(highindex - lowindex)

def main(args):
  parser = FileParser(1, 1, args[0])
  problem = parser.parse_problem()
  problem.set_case_logic(case_logic)
  problem.solve()
  problem.done()

if __name__ == "__main__":
  main(argv[1:])
