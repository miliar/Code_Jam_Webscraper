
d = "yhesocvxduiglbkrztnwjpfmaq"

def translate(c):
  if(c >= 'a' and c <= 'z'): return d[ord(c) - ord('a')]
  else: return c

N = int(raw_input())

for i in range(N):
  line = raw_input().strip()
  ans = ""
  for j in line: ans += translate(j)
  print "Case #"+str(i+1)+": "+ans
