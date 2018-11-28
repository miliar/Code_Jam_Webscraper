#!/usr/bin/env python

 

t = int(input())
a = 0
for i in range(1, t + 1):
  a+=1
  s = input()

  persue = False

  for m in range(len(s)):

    index = -1

    for i in range(len(s)-1):
      if s[i+1] < s[i]:
        index = i
        persue = True
        break

    if index == -1 :
     ret = s
    else :
      if index == 0:
        if s[index] == '1':
          num = ['9' for _ in range(len(s)-1)]
          ret = "".join(num)
        else:
          num = ['9' for _ in range(len(s)-1-index)]
          nine = "".join(num)
          ret = s[:index] + str(int(s[index])-1) + nine
      else :
       num = ['9' for _ in range(len(s)-1-index)]
       nine = "".join(num)
       ret = s[:index] + str(int(s[index])-1) + nine
    s = ret

    if persue == False :
      break

  print("Case #{}: {}".format(a, ret))
       