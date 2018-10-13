import math, sys

from math import pi

X = 1

# @arg inner_radius - integer in cm
# @res area - integer multiple of pi
def area_ring(inner_radius):
  return (2*inner_radius+1)


def main():
  parse()


def parse():
  file_input = sys.stdin.readlines()

  cases = eval(file_input.pop(0))
  for case in range(0,cases):
    r,t = map(lambda x: eval(x), file_input[case].strip().split())
    counter = 0
    while t >= 0:
      t = t - area_ring(r)
      if t >= 0:
        r += 2
        counter += 1
    print "Case #{0}: {1}".format(case+1,counter)


if __name__ == '__main__':
  main()
