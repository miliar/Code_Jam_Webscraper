#!/usr/bin/env python

if __name__ == '__main__':
  import sys
  import re

  f = open(sys.argv[1])
  n = int(f.readline())

  o_wins = "(.{4}|.{8}|.{12})?O{4}|((O.{3}){4})|(.{1,3}O(.{3}O){3})|(O.{4}O.{4}O.{4}O)|(.{3}O.{2}O.{2}O.{2}O)"
  x_wins = "(.{4}|.{8}|.{12})?X{4}|((X.{3}){4})|(.{1,3}X(.{3}X){3})|(X.{4}X.{4}X.{4}X)|(.{3}X.{2}X.{2}X.{2}X)"
  owins_re = re.compile(o_wins)
  xwins_re = re.compile(x_wins)

  for i in xrange(n):
    board = []
    board.extend([f.readline().strip() for j in xrange(4)])
    f.readline() # blank line
    assert len(board) == 4
#    print "\n".join(board)
    board_str = "".join(board)
    assert len(board_str) == 16
#    print board_str

    winner = "Game has not completed"
    if owins_re.match(board_str.replace('T', 'O')):
      winner = "O won"
    elif xwins_re.match(board_str.replace('T', 'X')):
      winner = "X won"
    elif not '.' in board_str:
      winner = "Draw"
  
    print "Case #%d: %s" % (i+1, winner)
  f.close()
