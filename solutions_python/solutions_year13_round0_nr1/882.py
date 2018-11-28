#!/usr/bin/env python2

from cStringIO import StringIO
from decimal import Decimal

class TicTacToe(object):
  def __init__(self, a, b, c, d):
    self.rows = [a, b, c, d]
    pass

  def __repr__(self):
    return '\n'.join(self.rows)

  def __str__(self):
    return repr(self)

  def winner(self, vector):
    if '.' in vector:
      return 'U'
    elif vector in [
        'XXXT', 'XXTX', 'XTXX', 'TXXX', 'XXXX'
        ] and vector in [
        'OOOT', 'OOTO', 'OTOO', 'TOOO', 'OOOO'
        ]:
       return 'D'
    elif vector in [
        'XXXT', 'XXTX', 'XTXX', 'TXXX', 'XXXX'
        ]:
      return 'X'
    elif vector in [
        'OOOT', 'OOTO', 'OTOO', 'TOOO', 'OOOO'
        ]:
      return 'O'
    else:
      return 'D'

  def reduce(self, results):
    if   'X' in results and 'O' in results:
      return 'D'
    elif 'X' in results:
      return 'X'
    elif 'O' in results:
      return 'O'
    elif 'U' in results:
      return 'U'
    else:
      return 'D'

  def row(self):
    results = [self.winner(row) for row in self.rows]
    return self.reduce(results)

  def col(self):
    vectors = [
        ''.join([row[i] for row in self.rows])
        for i in range(4)
        ]
    results = [self.winner(row) for row in vectors]
    return self.reduce(results)

  def diag(self):
    vectors = [
        ''.join([ self.rows[0][0], self.rows[1][1],
                  self.rows[2][2], self.rows[3][3],
                  ]),
        ''.join([ self.rows[0][3], self.rows[1][2],
                  self.rows[2][1], self.rows[3][0],
                  ])
        ]
    results = [self.winner(row) for row in vectors]
    return self.reduce(results)

  def outcome(self):
    return self.reduce([self.row(),
                        self.col(),
                        self.diag(),
                        ])

def decode_input(sb):
  outcomes = []

  count = int(sb.readline().strip())

  for i in xrange(count):
    a = sb.readline().strip()
    b = sb.readline().strip()
    c = sb.readline().strip()
    d = sb.readline().strip()
    _ = sb.readline()
    t = TicTacToe(a, b, c, d)
    outcomes.append(t.outcome())

  i = 1
  for o in outcomes:
    strings = {
        'D':'Draw',
        'X':'X won',
        'O':'O won',
        'U':'Game has not completed',
        }
    print('Case #%d: %s' % (i, strings[o]))
    i += 1

if __name__ == '__main__':
  import sys
  
  if len(sys.argv) > 1:
    decode_input(open(sys.argv[1]))
