import sys

sys.stdout = open("./small_output.txt", "w")

t = int(input())
for i in range(1, t + 1):
  fc = 0;
  n, k = raw_input().split(" ")
  nl = list(n)
  ik = int(k)
  for j in range(0, len(n) - ik + 1):
    if nl[j] == '-':
        for x in range(0, ik):
            if nl[j+x] == '-':
                nl[j+x] = '+'
            else:
                nl[j+x] = '-'
        fc += 1
  if '-' in nl:
      print('Case #{}: IMPOSSIBLE'.format(i))
  else:
      print('Case #{}: {}'.format(i,fc))
