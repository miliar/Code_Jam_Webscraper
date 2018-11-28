import sys

def rl():
  return sys.stdin.readline().strip()

def main():
  N = int(rl())
  for i in range(1, N+1):
    rows = [rl() for _ in range(4)]
    rl()
    s = 'Case #{}: '.format(i)
    done = False
    for row in rows:
      if all(c in 'XT' for c in row):
        print s+'X won'
        done = True
        break
      elif all(c in 'OT' for c in row): 
        print s+'O won'
        done = True
        break
    if done: continue
    for col in zip(*rows):
      if all(c in 'XT' for c in col):
        print s+'X won'
        done = True
        break
      elif all(c in 'OT' for c in col): 
        print s+'O won'
        done = True
        break
    if done: continue
    if all(c in 'XT' for c in 
             (row[i] for i, row in
                enumerate(rows))):
      print s+'X won'
      continue
    if all(c in 'OT' for c in 
             (row[i] for i, row in
                enumerate(rows))):
      print s+'O won'
      continue
    if all(c in 'XT' for c in 
             (row[3-i] for i, row in
                enumerate(rows))):
      print s+'X won'
      continue
    if all(c in 'OT' for c in 
             (row[3-i] for i, row in
                enumerate(rows))):
      print s+'O won'
      continue
    if '.' in ''.join(rows):
      print s+'Game has not completed'
    else:
      print s+'Draw'

if __name__ == '__main__':
    main()
