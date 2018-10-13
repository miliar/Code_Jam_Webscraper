import sys
cin = sys.stdin.readline
def readlist():
  return map(int, cin().split())
INF = sys.maxsize
NINF = -sys.maxsize - 1
#----------------------------------------------------------------------

# def get_consecutive_minuses(S):
#   cm = []
#   counter = 0
#   for c in S:
#     if c == '+':
#       if counter:
#         cm.append(counter)
#         counter = 0
#         continue
#     counter += 1
#   if counter:
#     cm.append(counter)
#   return cm

# T = int(cin())
# for _t in xrange(T):
#   S, K = cin().split()
#   K = int(K)
#   cm = get_consecutive_minuses(S)
#   answer = 0
#   for mcount in cm:
#     if mcount % K:
#       answer = "IMPOSSIBLE"
#       break
#     answer += mcount / K

#   print "Case #{}: {}".format(_t + 1, answer)


def flip(c):
  return '+' if c == '-' else '-'

T = int(cin())
for _t in xrange(T):
  S, K = cin().split()
  K = int(K)
  S = list(S)
  answer = 0
  for i in xrange(len(S)):
    if S[i] == '-':
      if i + K > len(S):
        answer = "IMPOSSIBLE"
        break
      answer += 1
      for j in xrange(i, i + K):
        S[j] = flip(S[j])

  print "Case #{}: {}".format(_t + 1, answer)
