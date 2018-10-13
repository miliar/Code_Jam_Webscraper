def pieces(num):
  result = []
  while num != 0:
    result.append(num % 10)
    num //= 10
  return result


cases = int(input())
for case in range(cases):
  num = int(input())
  if num // 10 == 0:
    tidyNum = num
  else:
    lastNum = pieces(num)
    for i in range(len(lastNum) - 1):
      if lastNum[i] < lastNum[i + 1]:
        lastNum[i + 1] -= 1
        for j in range(i, -1, -1):
          lastNum[j] = 9

    tidyNum = sum([base * 10 ** power for power, base in enumerate(lastNum)])
  
  print("Case #{}: {}".format(case + 1, tidyNum))

