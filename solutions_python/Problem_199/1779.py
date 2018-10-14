from __future__ import print_function
import fileinput

def flip(N, start, width):
  for i in range(start, start + width):
    if N[i] == "-":
      N[i] = "+"
    else:
      N[i] = "-"
  return N

def all_plus(N):
  for c in N:
    if c == "-":
      return False
  return True

f = fileinput.input()

T = int(f.readline())
for case in range(1, T + 1):
  line = f.readline().rstrip()
  pancakes, k = line.split()
  k = int(k)
  pancakes = list(pancakes)
  lenght = len(pancakes)
  max_turns = lenght - k + 1
  count = 0
  for i in range(0, max_turns):
    if pancakes[i] == "-":
      count += 1
      pancakes=flip(pancakes, i, k)
  if all_plus(pancakes):
    print("Case #"+str(case)+": "+str(count))
  else:
    print("Case #"+str(case)+": IMPOSSIBLE")
