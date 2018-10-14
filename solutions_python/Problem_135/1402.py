from sys import stdin

Q = int(stdin.readline())
for qq in xrange(Q):
  ass = set(range(1,17))
  for qqq in xrange(2):
    which = int(stdin.readline())-1
    for qqqq in xrange(which):
      stdin.readline()
    ass = ass & set(map(int,stdin.readline().split()))
    for qqqq in xrange(3-which):
      stdin.readline()
  if len(ass) == 0:
    print "Case #"+str(qq+1)+": Volunteer cheated!"
  elif len(ass) > 1:
    print "Case #"+str(qq+1)+": Bad magician!"
  else:
    print "Case #"+str(qq+1)+": "+str(list(ass)[0])