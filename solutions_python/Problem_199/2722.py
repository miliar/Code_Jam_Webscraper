# oversizedPancakeFlipper

def main():
  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
  # This is all you need for most Google Code Jam problems.
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    line   = input().strip().split(" ")
    case   = str(line[0])
    k      = int(line[1])
    length = len(case)
    # they're all already happy side up
    if ("-" not in case):
      print("Case #{}: {}".format(i, 0))
      continue
    # can only flip them all at once and they're not all blank side up
    elif (k == length and ("+" in case)):
      print("Case #{}: {}".format(i, "IMPOSSIBLE"))
    else:
      moves = 0
      solved = True
      while ("-" in case):
        index = case.find("-", 0, length - k + 1)
        if (index != -1):
          moves += 1
          for x in range(0, k):
            curChar = case[index + x]
            if (curChar == "-"):
              case = case[:index + x] + "+" + case[index + x + 1:]
              # case[index + x] = "+"
            else:
              assert(curChar == "+")
              case = case[:index + x] + "-" + case[index + x + 1:]
              # case[index + x] = "-"
        else:
          solved = False
          print("Case #{}: {}".format(i, "IMPOSSIBLE"))
          break
      if (solved):
        print("Case #{}: {}".format(i, moves))
  return

if __name__ == '__main__':
  main()