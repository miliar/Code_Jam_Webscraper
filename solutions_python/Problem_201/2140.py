#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(input())
def readfloat(): return float(input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, input().split())

N1 = 0
N2 = 1
INDEX = 2

def countLeft(pos, stalls):
  count = 0
  
  for i in range(pos-1, -1, -1):
    if stalls[i] == 'O': break
    count += 1
  
  return count

def countRight(pos, stalls):
  count = 0
  
  for i in range(pos+1, len(stalls)):
    if stalls[i] == 'O': break
    count += 1
  
  return count
  
def computeLsRs(stalls):
  ll = []
  for i in range(len(stalls)):
    if stalls[i] == 'O': continue
    ls = countLeft(i, stalls)
    rs = countRight(i, stalls)
    ll.append((min(ls, rs), max(ls, rs), len(stalls) -1 - i))
  return ll

def solve(N, K):
  
  N += 2
  
  stalls = N * ['.']
  stalls[0] = 'O'
  stalls[-1] = 'O'
  
  chosen = None
  
  #print(str(N) + ' ' + str(K))
  #print(stalls)
  for i in range(K):
    lsrs = computeLsRs(stalls)
    #print(lsrs)
    chosen = max(lsrs)
    i = N -1 - chosen[INDEX]
    stalls[i] = 'O'
    # y is max(LS, RS), and z is min(LS, RS) 
    y = chosen[N2]
    z = chosen[N1]
    #print(stalls)
    #print(str(y) + ' ' + str(z))
  
  #lsrs = computeLsRs(stalls)
  #chosen = max(lsrs)
  
  return y, z

def solve1(N, K):
  
  ll = [N]
  for i in range(K):
    # v // 2 + v % 2, v // 2
    v = ll.pop(0) - 1
    y, z = v // 2 + v % 2, v // 2
    ll.append(y)
    ll.append(z)
    ll = sorted(ll, reverse=True)
    
    #if ll != sorted(ll, reverse=True): print('ops')
  
  return y, z
if __name__ == '__main__':

  T = readint()
  for t in range(1, T+1):
    N, K = readlinearray(int)
    y, z = solve1(N, K)
    print('Case #%d: %d %d' % (t, y, z))
    