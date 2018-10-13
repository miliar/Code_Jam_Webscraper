def is_tidy(n):
  s = str(n)
  if len(s) == 1:
    return True
  for i in range(1, len(s)):
    if int(s[i]) < int(s[i-1]):
      return False
  return True

T = int(input())
for c in range(T):
  N = int(input())
  answer = ""
  while not is_tidy(N):
    S = list(str(N))
    S[-1] = "9"
    answer = answer + S[-1]
    N = int("".join(S[:-1]))
    N -=1
  answer = str(N) + answer
  answer = int(answer)
  print("Case #{}: {}".format(c+1, answer))