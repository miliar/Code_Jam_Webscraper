from itertools import *
from pprint import pprint


def main(f):
  fi = open(f + '.in')
  fo = open(f + '.out', 'w')

  T = int(fi.readline())
  for ti in range(T):
    cards = [[],[]]
    for i in range(2):
      choice = int(fi.readline().strip())      
      for j in range(1, 5):
        rcards = fi.readline().strip()
        if j == choice:
          rcards = rcards.split(' ')
          cards[i] = set([int(k) for k in rcards])

    possible = cards[0] & cards[1]
    out = 'Volunteer cheated!'
    if len(possible) == 1:
      out = str(list(possible)[0])
    elif len(possible) > 1:
      out = "Bad magician!"

    fo.write("Case #%d: %s\n" % ((ti+1), out) )
    print "Case #%d: %s" %  ((ti+1), out) 

if __name__ == "__main__":
  main('small_qr_a_1')