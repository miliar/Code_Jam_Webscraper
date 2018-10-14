# tidyNumbers

def main():
  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
  # This is all you need for most Google Code Jam problems.
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    n = int(input().strip())
    checkNum = n
    while (checkNum > 0):
      tempNum = checkNum
      prevDigit = 9
      place = 0
      done = True
      while(tempNum > 0):
        place += 1
        curDigit = tempNum % 10
        tempNum = tempNum // 10
        if (curDigit <= prevDigit):
          prevDigit = curDigit
          continue
        else:
          # place += 1
          done = False
          break
      if (done):
        print("Case #{}: {}".format(i, checkNum))
        # check out .format's specification for more formatting options
        break
      else:
        place = place - 1
        if (place >= 1):
          power = 10**place
          checkNum = (checkNum // power) * power - 1
        else:
          checkNum -= 1
  return

if __name__ == '__main__':
  main()