import sys
def canFinish(idx):
  for i in range(idx, n):
    if ken[i] > naomi[n - i + idx - 1]:
      return False
  return True

def deceitfulWarScore():
  i = 0
  while i < n:
    if canFinish(i):
      return n - i
    i += 1
  return 0

def warScore():
  taken = [False]*n
  ans   = n
  i, j = 0, n - 1
  while i < n:
    while j >= 0:
      if not taken[j] and ken[j] > naomi[i]:
        break
      j -= 1
    i += 1
    if j >= 0:
      ans -= 1
      taken[j] = True
  return ans

sys.stdin  = open("D-large.in")
sys.stdout = open("D-large.out", "w")
t = int(raw_input())
for case_no in range(1, t+1):
  n = int(raw_input())
  naomi = map(float, raw_input().split())
  ken   = map(float, raw_input().split())
  naomi.sort(); ken.sort(reverse=True);
  #print naomi
  #print ken  
  print "Case #%d: " % (case_no), deceitfulWarScore(), warScore()