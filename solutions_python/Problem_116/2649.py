#!/usr/bin/env python3

def main():
  N = int(input())
  
  for no in range(N):
    print("Case #%d: %s" % (no + 1, solve()))

def solve():
  data = [input() for i in range(5)]
  
  for side in ('X', 'O'):
    if (any(all(data[i][j] in (side, 'T') for j in range(4)) for i in range(4)) or
        any(all(data[j][i] in (side, 'T') for j in range(4)) for i in range(4)) or
        all(data[j][j] in (side, 'T') for j in range(4)) or
        all(data[j][3-j] in (side, 'T') for j in range(4))):
      return "%s won" % side

  if '.' in ''.join(data[0:4]):
    return "Game has not completed"
  else:
    return "Draw"

if __name__ == '__main__':
  main()
