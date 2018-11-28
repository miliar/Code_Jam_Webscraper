#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import copy

def check(rows, i, j, N, K):
  K -= 1
  target = rows[i][j]
  if (target != '.'):
    # タテチェック
    tmp_cnt = {'R':0, 'B':0}
    for v1 in range(1, i):
      if rows[i-v1][j] == target:
        tmp_cnt[target] += 1
      else:
        break
    for v2 in range(1, N-i):
      if rows[i+v2][j] == target:
        tmp_cnt[target] += 1
      else:
        break
    if tmp_cnt[target] >= K:
      return target

    # 横チェック
    tmp_cnt = {'R':0, 'B':0}    
    for h1 in range(1, j):
      if rows[i][j-h1] == target:
        tmp_cnt[target] += 1
      else:
        break
    for h2 in range(1, N-j):
      if rows[i][j+h2] == target:
        tmp_cnt[target] += 1
      else:
        break
    if tmp_cnt[target] >= K:
      return target

    # 斜めチェック (左上から右下)
    tmp_cnt = {'R':0, 'B':0}
    for dl1 in range(1, min(i,j)):
      if rows[i-dl1][j-dl1] == target:
        tmp_cnt[target] += 1
      else:
        break
    for dl2 in range(1, min(N-i,N-j)):
      if rows[i+dl2][j+dl2] == target:
        tmp_cnt[target] += 1
      else:
        break
    if tmp_cnt[target] >= K:
      return target

    # 斜めチェック (右上から左下)
    tmp_cnt = {'R':0, 'B':0}
    for dr1 in range(1, min(N-i, j)):
      if rows[i+dr1][j-dr1] == target:
        tmp_cnt[target] += 1
      else:
        break
    for dr2 in range(1, min(i,N-j)):
      if rows[i-dr2][j+dr2] == target:
        tmp_cnt[target] += 1
      else:
        break
    if tmp_cnt[target] >= K:
      return target
      
  return None
  
def main():
  f = sys.stdin
  T = int(f.readline())
  for t in range(T):
    (N, K) = map(lambda x:int(x), f.readline().split(' '))
    rows = []
    for j in range(N):
      rows.append(f.readline())

    # rotate
    columns = []
    for j in range(N):
      column = [row[j] for row in rows]
      column = column[::-1]
      columns.append(column)
    rows = columns

    # gravity
    for j in range(1, N+1): # 行を下から走査
      for k in range(N):  # 行のk文字目
        if rows[-j][k] != '.':
          for l in range(1, j):  # 現在の行より下の行
            if rows[-l][k] == '.':
              (rows[-j][k], rows[-l][k]) = (rows[-l][k], rows[-j][k])
              break

    # check
    status = {'R':False, 'B':False}
    for i in range(N):    # 行
      for j in range(N):  # 列
        result = check(rows, i, j, N, K)
        if result:
          status[result] = True
      if status['R'] and status['B']:
        break

    # output result
    result = "Neither"
    if status['R'] and status['B']:
      result = 'Both'
    elif status['R']:
      result = 'Red'
    elif status['B']:
      result = 'Blue'
    print "Case #%d: %s" % (t+1, result)

if __name__ == '__main__':
  main()
