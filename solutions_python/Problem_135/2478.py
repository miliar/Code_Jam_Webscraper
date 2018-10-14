cases = int(raw_input())
for z in xrange(1,(cases+1)):
  ans1 = int(raw_input())
  config1 = [1,2,3,4]
  for y in xrange(4):
    config1[y] = map(int, raw_input().split())
  ans2 = int(raw_input())
  config2 = [1,2,3,4]
  for y in xrange(4):
    config2[y] = map(int, raw_input().split())
  intersect = list(set(config1[ans1-1]) & set(config2[ans2-1]))
  if(len(intersect) == 0):
    print "Case #" + str(z) + ": Volunteer cheated!"
  elif(len(intersect) > 1):
    print "Case #" + str(z) + ": Bad magician!"
  else:
    print "Case #" + str(z) + ": " + str(intersect[0])# your code goes here
