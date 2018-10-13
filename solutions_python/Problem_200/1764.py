import sys
import math

# cosine of two vectors
def calc_num(s):
  i = 0
  while (i < len(s)-1):
    if int(s[i]) > int(s[i+1]):
      break
    i += 1
  if i == len(s)-1:
    return s
  j = i-1
  while (j >= 0):
    if int(s[j]) <= int(s[i])-1:
      break
    j -= 1
  target_len = len(s)
  if j == -1:
    res = str(int(s[0])-1)
  else:
    res = s[:j+1] + str(int(s[i])-1)
  while len(res) < target_len:
    res += "9"
  if res[0] == '0':
    res = res[1:]
  return res
	

in_file = open(sys.argv[1])
num = int(in_file.readline().strip())
cnt = 0
for line in in_file:
  s = line.strip()
  res = calc_num(s)
  print "Case #"+str(cnt+1)+": " + str(res)
  cnt += 1
  if cnt == num:
    break
in_file.close()
