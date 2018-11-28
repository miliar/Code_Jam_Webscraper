import sys
import math

# cosine of two vectors
def calc_num(s, k):
  res = 0
  cnt = [0] * len(s)
  for i in range(len(s)):
    if (s[i]=='+' and cnt[i]%2==0) or (s[i]=='-' and cnt[i]%2==1):
      continue
    else:
      if (i+k > len(s)):
        return -1
      res += 1
      for j in range(i, i+k):
        cnt[j] += 1
  return res
	

in_file = open(sys.argv[1])
num = int(in_file.readline().strip())
cnt = 0
for line in in_file:
  s, k = line.strip().split()
  res = calc_num(s, int(k))
  if res >= 0:
    print "Case #"+str(cnt+1)+": " + str(res)
  elif res == -1:
    print "Case #"+str(cnt+1)+": IMPOSSIBLE"
  cnt += 1
  if cnt == num:
    break
in_file.close()
