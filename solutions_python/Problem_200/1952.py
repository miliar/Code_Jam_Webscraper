import sys

#1000
def solve(n):
  if is_okay(n):
    return n
  ds = []
  for digit in str(n):
    ds.append (int(digit))

  for x in range(len(ds)-1):
    if ds[x]>ds[x+1]:
      for y in range(len(ds)-x-1):
        ds[x+y+1]=9
      ds[x]-=1
      break
  n = int(''.join(map(str,ds)))
  return solve(n)


def is_okay(n):
  return ''.join(sorted(str(n)))==str(n)


name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = int(input())
    r = solve(line)


    print("Case #" + str(testCase) + ": " + str(r))

