import unittest
from expecter import expect
import sys

def solve_osmos(n, S):
  S.sort()
  changes = 0
  minp = []
  minp.append(len(S))
  while len(S) > 0:
    if (len(S) == 1) and (n <= S[0]):
      S.pop(0)
      changes += 1
    elif (n == 1):
      S.pop(0)
      changes += 1
    elif n <= S[0]:
      minp.append(len(S) + changes)
      np = n
      cp = 0
      while np <= S[0]:
        np = 2 * np - 1
        cp += 1
      if cp > len(S):
        changes += len(S)
        S = []
      else:
        n = np
        changes += cp
    elif n > S[0]:
      n += S.pop(0)
  return min([changes] + minp)

def calc(data):
  results = []
  while not data[0]: data.pop(0)
  cases = int(data.pop(0))
  for case in range(cases):
    n, count = map(int, data.pop(0).split())
    motes = map(int, data.pop(0).split()[:count])
    results.append("Case #%i: %i" % (case + 1, solve_osmos(n, motes)))
  return "\n".join(results)

if __name__ == "__main__":
  print calc(sys.stdin.readlines())

testdata = """
4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1
"""

test_result = """Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 4"""

class TestIt(unittest.TestCase):
  def test_osmos(self):
    expect(calc(testdata.split("\n"))) == test_result
  def test_solve_osmos(self):
    expect(solve_osmos(2, [1,10,100])) == 2
  def test_solve_osmos_too_large(self):
    expect(solve_osmos(2, [100,10,100])) == 3
  def test_solve_osmos_possibly_too_large(self):
    expect(solve_osmos(2, [100,4,100])) == 3
