from io import open
from fractions import Fraction
import math

def process(inp):
  nr, dr = map(int, inp.readline().split('/'))
  nrSimple, drSimple = Fraction(nr, dr).numerator, Fraction(nr, dr).denominator
  while nrSimple != 1:
    nr = nrSimple-1
    dr = drSimple
    nrSimple, drSimple = Fraction(nr, dr).numerator, Fraction(nr, dr).denominator
  hierarchy = math.log(drSimple, 2)
  if int(hierarchy) == hierarchy:
    return int(hierarchy)
  else:
    return "impossible"

def output(strOut, out):
  print strOut
  out.write(u"{}\n".format(strOut))

def main():
  inp = open("input.txt")
  out = open("output.txt", "wb+")
  tC = int(inp.readline())
  tc = tC
  while tc > 0:
    tc -= 1
    ans = process(inp)
    output(u"Case #{}: {}".format(tC-tc, ans), out)
  inp.close()
  out.close()

if __name__ == "__main__":
  main()
