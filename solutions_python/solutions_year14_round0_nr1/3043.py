a = input()

b = open("file1", 'w')

for i in xrange(a):
  x = input()
  set1 = set()
  set2 = set()
  for j in range(4):
    row = set(map(int, raw_input().split(' ')))
    if j+1 == x: set1 = row

  y = input()
  for j in range(4):
    row = set(map(int, raw_input().split(' ')))
    if j+1 == y: set2 = row


  resp = set1 & set2

  if len(resp) == 1:
    b.write("Case #%d: %d\n" % (i+1, resp.pop()))
  elif len(resp) > 1: 
    b.write("Case #%d: Bad magician!\n" % (i+1))
  else:
    b.write("Case #%d: Volunteer cheated!\n" % (i+1))

b.close()
