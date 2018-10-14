x = int(raw_input())
for i in range(x):
  print "Case #" + str(i+1) + ":",
  number = raw_input()
  last = 0
  newone = ""
  failingone = ""
  skipper = False
  for i in number:
    if skipper or (int(i) < last):
      skipper = True
      failingone += i
    else:
      newone += i
      last = int(i)
  if (not skipper):
    print newone
  else:
    if int(newone[-1]) != 1:
      ans = ""
      for i in newone:
        if i!=newone[-1]:
          ans +=i
        else:
          ans +=str(int(newone[-1]) - 1)
          break
      ans += "9" * (len(number)-len(ans))
      print ans
    else:
      print "9" * (len(number)-1)
    