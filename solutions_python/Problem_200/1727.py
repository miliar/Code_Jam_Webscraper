for tc in range(input()):
  number = list(raw_input())
  for i in range(len(number) - 1):
    for j in range(len(number) - 1):
      if int(number[j]) > int(number[j+1]):
        number[j] = str(int(number[j]) - 1)
        for k in range(j+1, len(number)):
          number[k] = '9'
  print "Case #" + str(tc + 1) + ": " + str(int("".join(number)))