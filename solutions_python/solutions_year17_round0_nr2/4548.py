# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import sys
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s_num = list(input())
  numbers = [int(s) for s in s_num]  # read a list of integers, 2 in this case
  index = 0
  while True:
    if index == (len(numbers) -1):
      break
    if numbers[index] <= numbers[index+1]:
      index += 1
    else:
      if numbers[index] > 0:
        numbers[index] = numbers[index] -1
        # 一つ上の位よりしたになっていないかのチェック
        if numbers[index-1] > numbers[index]:
          c = 0
          p = -1
          while numbers[index+p] >= numbers[index+c]:
            if index+p == 0:
              numbers[index+p] = numbers[index+p] -1
              for j in range(index+p+1, len(numbers)):
                numbers[j] = 9
              break
            elif index+p < 0:
              for j in range(index+1, len(numbers)):
                numbers[j] = 9
              break
            numbers[index+p] = numbers[index+p] -1
            c -= 1
            p -= 1
            
        for j in range(index +1, len(numbers)):
          numbers[j] = 9
      else: 
        # 一つ上の位を下げて自分以下を９へ
        numbers[index-1] = numbers[index-1] -1
        for j in range(index, len(numbers)):
          numbers[j] = 9

  result = int(''.join([str(i) for i in numbers]))
  print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options