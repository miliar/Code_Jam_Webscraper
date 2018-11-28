fi = open('A-small-attempt0.in','r')
fo = open('A-small-attempt0.out','w')
t = int(fi.readline())
for i in range(0, t):
  firstRowNumber = int(fi.readline())
  for j in range(0, firstRowNumber-1):
    fi.readline()
  firstRow = map(int, fi.readline().split())
  for k in range(0, 4-firstRowNumber):
    fi.readline()
  secondRowNumber = int(fi.readline())
  for j in range(0, secondRowNumber-1):
    fi.readline()
  secondRow = map(int, fi.readline().split())
  for k in range(0, 4-secondRowNumber):
    fi.readline()
  
  firstSet = set(firstRow)
  secondSet = set(secondRow)

  intersection = firstSet & secondSet

  if len(intersection) == 0:
    print 'Case #%d: Volunteer cheated!' % (i+1)
  elif len(intersection) == 1:
    print 'Case #%d: %d' % ((i+1), intersection.pop())
  else:
    print 'Case #%d: Bad magician!' % (i+1)

fi.close
fo.close