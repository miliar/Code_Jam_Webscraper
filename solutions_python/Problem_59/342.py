#!/usr/bin/python -tt
import sys
import os

def main():
  T = int(raw_input())
  
  for i in range(1, T+1):
    N, M = map(int, raw_input().split())
    answer = 0
    existing = ['/']
    for n in range(N): 
      existing.append(raw_input())
    for m in range(M): 
      path = raw_input()
      if not path in existing: 
        answer += 1
        existing.append(path)
      parent = os.path.dirname(path)
      while not parent in existing: 
        answer += 1
        existing.append(parent)
        parent = os.path.dirname(parent)
    print ('Case #'+str(i)+': ' + str(answer))

if __name__ == '__main__':
  main()
