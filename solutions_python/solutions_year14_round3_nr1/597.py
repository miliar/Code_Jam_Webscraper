import sys
import re

def readcases():
  f = open(sys.argv[1], 'r')
  t = int(f.readline())

  cases = [];
  r = re.compile('[ \n/]+')
  for i in xrange(t):
    data = map(int, r.split(f.readline())[:-1])
    cases.append({'p': data[0], 'q': data[1]})
  f.close()
  return cases
def do_stuff():
  cases = readcases()
  o = open('out.txt', 'w')
  for i in xrange(len(cases)):
    out = 'Case #' + str(i+1) + ': '
    case = cases[i]
    # TODO 
    test = case['q']
    impossible = False
    while 1:
      if test == 2:
        break
      if test % 2:
        impossible = True
        break
      test /= 2
    if impossible:
      out += 'impossible'
    else:
      q = case['q']
      gen = 1
      while 1:
        if case['p'] >= q/2:
          break
        q /= 2
        gen += 1
        if q <= 1:
          break
      out += str(gen)
    #
    out += '\n'
    print out
    o.write(out);
  o.close();

def main():
  if len(sys.argv) != 2:
    print 'Usage: python kaboom.py <input>'
  else:
    do_stuff()
if __name__ == '__main__':
  main()
