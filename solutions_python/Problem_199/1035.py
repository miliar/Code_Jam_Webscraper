def flip_char(c):
  if (c == "+"):
    return "-"
  else:
    return "+"


def switch(s,p,l):
  res = ""
  for i in range(len(s)):
    if ((i >= p) and (i < p+l)):
      res += flip_char(s[i])
    else:
      res += s[i]
  return res

def solution(pattern,size):
  pos = 0
  flips = 0
  while (pos <= (len(pattern) - size)):
    if (pattern[pos] == "+"):
      pos += 1
    else:
      flips += 1
      pattern = switch(pattern,pos,size)
  if (pattern.find("-") >= 0):
    return "IMPOSSIBLE"
  else:
    return "%d" %flips

t = int(raw_input())
for i in xrange(1, t + 1):
  pattern,size= raw_input().split(" ")
  size = int(size)
  res = solution(pattern,size)
  case_str = "Case #%d: " %i
  print case_str + res
