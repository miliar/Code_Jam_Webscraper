#!/usr/bin/python
import sys

inp = [l.strip() for l in sys.stdin]
T = int(inp[0])
l = 1
for t in range(T):
  board = inp[5*t+1:5*t+5]
  #print board

  xh = [0]*4
  xv = [0]*4
  xd1 = 0
  xd2 = 0

  oh = [0]*4
  ov = [0]*4
  od1 = 0
  od2 = 0

  cnt = 0
  for r in range(4):
  	for c in range(4):
  		ch = board[r][c]
  		isO = ch=='T' or ch=='O'
  		isX = ch=='T' or ch=='X'
  		if isO:
  			oh[r]+=1
  			ov[c]+=1
  			if r==c:
  				od1 += 1
  			if r+c==3:
  				od2 += 1
  		if isX:
  			xh[r]+=1
  			xv[c]+=1
  			if r==c:
  				xd1 += 1
  			if r+c==3:
  				xd2 += 1
  		if isO or isX:
  			cnt += 1

  #print xh, xv, oh, ov
  l += 1
  xh.sort()
  oh.sort()
  xv.sort()
  ov.sort()
  s = "WTF"
  if xh[3]==4 or xv[3]==4 or xd1==4 or xd2==4:
  	s = "X won"
  elif oh[3]==4 or ov[3]==4 or od1==4 or od2==4:
  	s = "O won"
  elif cnt==16:
  	s = "Draw"
  else:
  	s = "Game has not completed"

  print "Case #%d: %s" % (t+1, s)

