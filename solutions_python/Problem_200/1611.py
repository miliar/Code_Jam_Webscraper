t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  ss = raw_input()
  s = list(ss)
  if len(s) < 2:
    ss = "".join(s)
    print "Case #"+str(i)+": "+ss
  else:
    pointer = 0
    for q in range(len(s) - 1):
      if s[q] > s[q+1]:
        pointer = q
        for j in reversed(range(int(q))):
          if int(s[j]) == int(s[pointer]):
            pointer = j
        for k in range(pointer+1, len(s)):
          s[k] = "9"
        s[pointer] =  str (int(s[pointer]) - 1)
    if s[0] is "0":
      del s[0]
      for p in s:
        p = "9"
    ss = "".join(s)
    print "Case #" + str(i) + ": " + ss

    
    
  

