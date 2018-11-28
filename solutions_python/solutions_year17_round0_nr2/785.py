t = int(input())
for i in range(1, t + 1):
  number = int(input())

  j = 0
  s = str(number)[::-1]

  while j < len(s) - 1:
    c1 = s[j]
    c2 = s[j + 1]

    if int(c1) < int(c2):
      new_s = '0' * (j + 1)
      s = new_s + s[j + 1:]
      s = s[::-1]
      number = int(s) - 1
      s = str(number)[::-1]
      j = 0
    else:
      j += 1

  print("Case #{}: {}".format(i, number))