import sys


input = open(sys.argv[1], 'r')

tests = int(input.readline())


for i in range(0, tests):
  row = input.readline().rstrip().split(' ')
  row = map(float,row)

  # C F X
  c = row[0]
  f = row[1]
  x = row[2]


  seconds = 0.0
  rate = 2.0


  if x < c:
    seconds += float(x/rate)
    print "Case #%d: %.7f" % (i+1,seconds)
    continue


  while True:

    nowS = float(x / rate)

    s = float(c / rate)

    s1 = float(x / (rate + f))

    total = s1 + s

    #dont buy
    if nowS < total:
      bestTime = seconds + nowS
      print "Case #%d: %.7f" % (i+1,bestTime)
      break

    rate += f

    seconds += s
