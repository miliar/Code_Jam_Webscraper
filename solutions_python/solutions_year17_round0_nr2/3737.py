def nearestTidy(x):
  prev = int(x[0])
  first = 0
  res = ''
  for idx,i in enumerate(x[1:]):
    cur = int(i)
    #print "xm " + str(cur) + " " + str(idx) + " " + str(prev)
    if cur > prev:
      prev = cur
      first = idx + 1
      continue
    elif cur == prev:
      continue
    else:
      if first == 0 and x[0] == '1':
        for j in range(len(x) - 1):
          res += str(9)
      else:
        for j in x[:first]:
          res += j
        res += str(prev - 1)
        for j in x[first+1:]:
          res += '9'
      return res
  return x

if __name__ == '__main__':
  tests = input()
  for i in range(tests):
    x = raw_input()
    print "Case #" + str(i + 1) +": " + nearestTidy(x)

      

