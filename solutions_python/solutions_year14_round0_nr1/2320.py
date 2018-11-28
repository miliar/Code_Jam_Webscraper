import sys

input = open(sys.argv[1], 'r')

tests = int(input.readline())


for i in range(0, tests):
  board1 = []
  board2 = []

  firstAns = int(input.readline())

  for j in range(0,4):
    row = input.readline().rstrip().split(' ')
    row = map(int,row)

    board1.append(row)

  secondAns = int(input.readline())



  for j in range(0,4):
    row = input.readline().rstrip().split(' ')
    row = map(int,row)

    board2.append(row)

  line1 = board1[firstAns-1]
  line2 = board2[secondAns-1]

  # 3 volunteer cheated
  match = False
  bad = False
  n = 0

  for j in range(0,4):
    for k in range(0,4):
      if line1[j] == line2[k]:
        if match:
          bad = True

        match = True
        n = line1[j]

  if match and not bad:
    print "Case #%d: %d" % (i+1, n)
  elif bad:
    print "Case #%d: Bad magician!" % (i+1)
  elif not match:
    print "Case #%d: Volunteer cheated!" % (i+1)

  del board1
  del board2
  del line1
  del line2
