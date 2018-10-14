#!/usr/bin/env python3

def flip(S,K):
  if len(S)<K:
    return False
  if len(S)==K:
    return flip_front(S,K)
  
  nfront = 0
  nback = 0
  for i in range(K):
    if S[i] == '-':
      nfront = nfront+1
    if S[-1-i] == '-':
      nback = nback+1

  if nback > nfront:
    return flip_back(S,K)
  else:
    return flip_front(S,K)

def flip_front(S,K):
  S = list(S)
  for i in range(K):
    if S[i]=='-':
      S[i] = '+'
    else:
      S[i] = '-'
  return ''.join(S)

def flip_back(S,K):
  S = list(S)
  for i in range(1,K+1):
    if S[-i]=='-':
      S[-i] = '+'
    else:
      S[-i] = '-'
  return ''.join(S)

T = int(input())

for i in range(1,T+1):
 
  line = input()
  S = line.split()[0]
  K = int(line.split()[1])

  S = S.strip('+')
  for ncount in range(len(S)+1):
    if len(S)==0:
      print("Case #{}: {}".format(i,ncount))
      break
    S = flip(S,K)
    if S:
      S = S.strip('+')
    else:
      print("Case #{}: IMPOSSIBLE".format(i))
      break
