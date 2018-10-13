# Input
# 4
# 6 2 0 2 0 2 0
# 3 1 0 2 0 0 0
# 6 2 0 1 1 2 0
# 4 0 0 2 0 0 2
#
# Output
# Case #1: RYBRBY
# Case #2: IMPOSSIBLE
# Case #3: YBRGRB
# Case #4: YVYV

#will work for the small dataset

def mayArrange(N, R, O, Y, G, B, V):

  limit = N/2.0
  for color in [R, O, Y, G, B, V]:
    if color > limit:
      return False
  return True

def fill(stalls, index_start, index_max, times, letter):
  i = index_start
  for j in range(times):
    if stalls[i] != '':
      i+=1
    stalls[i] = letter
    i = (i+2)%index_max
  return i

def arrange(N, R, O, Y, G, B, V):
  stalls = ['']*N
  letters = [(R, 'R'), (Y, 'Y'), (B, 'B')]
  letters.sort(key=lambda tup: tup[0])
  i = 0
  for letter in letters:
    i = fill(stalls, i, N, letter[0], letter[1])
  arrangement = ''
  for letter in stalls:
    arrangement += letter
  return arrangement


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  N, R, O, Y, G, B, V = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  arrangement = 'IMPOSSIBLE'
  if mayArrange(N, R, O, Y, G, B, V):
    arrangement = arrange(N, R, O, Y, G, B, V)
  print("Case #{}: {}".format(i, arrangement))
  # check out .format's specification for more formatting options