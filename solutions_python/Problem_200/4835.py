t = int(input())
for case in range(1, t + 1):
  last = int(input())
  ordered = False
  while ordered == False and last > 0:
    if last < 10:
        break
    digits = str(last)
    for i in range(len(digits) - 2, -1, -1):
        digits = str(last)
        if int(digits[i]) <= int(digits[i+1]):
            ordered = True
        else:
            ordered = False
            last -= 1
        if ordered == False:
            break

  print("Case #{}: {}".format(case, last))
