T = int(raw_input())
for t in range(1,T+1):
  N,X = map(int,raw_input().split())
  S = map(int,raw_input().split())
  S.sort()
  sp = 0
  lp = len(S)-1
  count = 0
  while sp<lp+1:
    if sp!=lp and S[sp] + S[lp] <=X:
      count+= 1
      sp +=1
      lp -=1
    else:
      count += 1
      lp -=1
  print "Case #"+str(t)+": "+str(count)
