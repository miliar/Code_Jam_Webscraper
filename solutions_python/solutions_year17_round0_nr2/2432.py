t = int(raw_input())  # read a line with a single integer

for count in xrange(1, t + 1):
  S = raw_input()
  New_No = int(S)
  Slen = len(S)
  i = Slen
  counter = 0
  factor = 1
  while(1):
      if Slen-counter-1 <= 0:
          break
      factor *= 10
      i -= 1
      counter +=1
      if S[i] == '0':
          New_No = New_No - (1 + New_No % (factor))
      elif S[i] >= S[i-1]:
          continue
      else:
          New_No = New_No - (1 + (New_No % (factor)))
      S = str(New_No)
      Slen = len(S)
  print "Case #{}: {}".format(count, New_No)
