#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import stdin, stdout

def main():
  def calc(s, symbol):
    result = 0
    for c in s:
      if c in (symbol, 'T'):
        result += 1
    return result

  def check(board):
    # check horizontals
    xxs = []
    oos = []
    for s in board:
      xxs.append(calc(s, 'X'))
      oos.append(calc(s, 'O'))
    if 4 in xxs:
      return 'X won'
    elif 4 in oos:
      return 'O won'

    # check verticals
    xxs = []
    oos = []
    for i in range(4):
      xxs.append(calc(''.join([s[i] for s in board]), 'X'))
      oos.append(calc(''.join([s[i] for s in board]), 'O'))
    if 4 in xxs:
      return 'X won'
    elif 4 in oos:
      return 'O won'

    # check diagonals
    if calc(''.join([board[i][i] for i in range(4)]), 'X') == 4 or \
        calc(''.join([board[i][3 - i] for i in range(4)]), 'X') == 4:
      return 'X won'
    elif calc(''.join([board[i][i] for i in range(4)]), 'O') == 4 or \
        calc(''.join([board[i][3 - i] for i in range(4)]), 'O') == 4:
      return 'O won'

    # check for draw
    if '.' in ''.join(board):
      return 'Game has not completed'

    return 'Draw'

  t = int(stdin.readline())
  for i in xrange(1, t + 1):
    board = [stdin.readline().strip() for j in range(4)]
    print 'Case #%i: %s' % (i, check(board))
    stdin.readline()

if __name__ == '__main__':
  main()
