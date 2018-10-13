from sys import stdin

T = int(stdin.readline().strip())

def is_tidy(num):
  num_s = str(num)
  for i in range(len(num_s) - 1):
    if num_s[i] > num_s[i+1]:
      return False
  return True

def greatest_tidy(N):
  original = int(N)
  g_tidy = original
  while not is_tidy(g_tidy):
    g_tidy -= 1
  return g_tidy

for i in range(T):
  N = stdin.readline().strip()
  print("Case #{0}: {1}".format(i + 1, greatest_tidy(N)))
