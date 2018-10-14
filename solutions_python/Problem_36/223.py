import sys

mem = []

target = "welcome to code jam"

def dp(sentence, offset):
  if mem[len(sentence)][offset] != -1:
    return mem[len(sentence)][offset]
  if len(sentence) == 0 and offset == len(target):
    return 1
  if len(sentence) == 0:
    return 0
  ct = 0;
  if offset != len(target) and sentence[0] == target[offset]:
    ct += dp(sentence[1:], offset+1)
  ct += dp(sentence[1:], offset)
  mem[len(sentence)][offset] = ct
  return ct

n = int(sys.stdin.readline())
for i in range(n):
  mem = [-1]*600;
  for j in range(600):
    mem[j] = [-1]*50;
    for k in range(50):
      mem[j][k] = -1;
  sentence = (sys.stdin.readline())[:-1]
  print "Case #%d: %04d" % (i+1, dp(sentence, 0) % 10000)
