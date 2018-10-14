import sys


def mowlawn(pattern):
  lawn = []
  for i in range(len(pattern)):
    row = [int(c) for c in pattern[i].split(' ')]
    largest = max(row)
    lawn.append([largest]*len(row))
  for i in range(len(pattern[0].split(' '))):
    column = [int(line.split(' ')[i]) for line in pattern]
    largest = max(column)
    for j in range(len(pattern)):
      lawn[j][i] = min(largest, lawn[j][i])
  return lawn


if __name__=="__main__":
  lines = sys.stdin.readlines()
  i = 1
  case = 1
  while i < len(lines):
    first = lines[i].strip().split(' ')
    N = int(first[0])
    M = int(first[1])
    pattern = [line.strip() for line in lines[i+1:i+1+N]]
    possible = mowlawn(pattern)
    lawn = [' '.join([str(n) for n in line]) for line in possible]
    print "Case #{}: {}".format(case, "YES" if lawn == pattern else "NO")
    case += 1
    i += N+1
