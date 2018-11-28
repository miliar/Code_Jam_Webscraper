#!/usr/bin/env python3

import sys

def read_configuration():
  tmp = sys.stdin.readline().split()
  return (int(tmp[0]), list(map(int, tmp[1])))

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  
  for t in range(1, T+1):
    S_max, audience = read_configuration()
    
    total_added, standing = 0, audience[0]
    for shyness in range(1, S_max+1):
      added = 0
      if audience[shyness] > 0 and standing < shyness:
        added += shyness - standing
        total_added += added
      standing += audience[shyness] + added
    
    print('Case #{}: {}'.format(t, total_added))

