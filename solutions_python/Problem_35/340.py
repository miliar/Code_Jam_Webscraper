#!/usr/bin/env python
import sys

max_altitude = 10000

alphabet = []

data = []
flag = []
(H, W) = (0, 0)

def main():
  global data, flag, H, W, alphabet

  T = int(sys.stdin.readline().strip())
  for case in range(1, T + 1):
    alphabet = []
    for i in range(26):
      alphabet.append(chr(ord('a') + i))
    
    (H, W) = map(lambda x:int(x), sys.stdin.readline().strip().split(' '))
    data = []
    for i in range(H):
      data.append(sys.stdin.readline().strip().split(' '))

    flag = []
    for i in range(H):
      flag.append([False] * W)

    for i in range(H):
      for j in range(W):
        if not flag[i][j]:
          travel(i, j)

    print 'Case #' + str(case) + ':'
    for i in range(H):
      row = flag[i][0]
      for j in range(W - 1):
        row += ' ' + flag[i][1 + j]
      print row



def travel(i, j):
  global data, flag, H, W, alphabet

  neighbors = []
  values = []
  if i - 1 >= 0:
    neighbors.append((i-1, j))
    values.append(data[i-1][j])
  if j - 1 >= 0:
    neighbors.append((i, j-1))
    values.append(data[i][j-1])
  if j + 1 < W:
    neighbors.append((i, j+1))
    values.append(data[i][j+1])
  if i + 1 < H:
    neighbors.append((i+1,j))
    values.append(data[i+1][j])
    
  if len(values) == 0:
    flag[i][j] = alphabet.pop(0)

  elif min(values) < data[i][j]:
    des = neighbors[values.index(min(values))]
    di = des[0]
    dj = des[1]
    if flag[di][dj]:
      flag[i][j] = flag[di][dj]
    else:
      flag[i][j] = travel(di, dj)

  else:
    if not flag[i][j]:
      flag[i][j] = alphabet.pop(0)

  return flag[i][j]


          

if __name__ == '__main__':
  main()
