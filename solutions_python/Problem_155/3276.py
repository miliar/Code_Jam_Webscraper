for case in range(int(input())):
  max, data = input().split(" ")
  current    = 0
  additional = 0
  for i in range(int(max)+1):
    if current < i:
      required   = i - current
      current    = current    + required
      additional = additional + required
    current = current + int(data[i])
  print("Case #"+str(case+1)+": "+str(additional))
