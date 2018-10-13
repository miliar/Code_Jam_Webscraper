import unittest
import sys
from expecter import expect
from math import pi

def tvol(r):
  return round(((pi*(r+1)**2 - pi*r**2)/pi),4)

def circles(r,t):
  count = 0
  while t >= 0:
    count += 1
    t -= tvol(r)
    r += 2
  return count - 1 if count > 0 else 1

def calc(data):
  while not data[0]: data.pop(0)
  cases = int(data.pop(0))
  output = ''
  for i in range(cases):
    r, t = map(int, data.pop(0).split())
    output += "Case #%i: %i\n" % (i+1, circles(r,t))
  return output

if __name__ == "__main__":
  print calc(sys.stdin.readlines())

testdata = """
3
1 9
1 10
3 40
"""

test_result = """Case #1: 1
Case #2: 2
Case #3: 3
"""

class TestIt(unittest.TestCase):
  def test_it(self):
    expect(calc(testdata.split('\n'))) == test_result
