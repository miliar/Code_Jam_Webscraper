"""
Solve the magic trick.
"""

inFile = [line.rstrip() for line in open('../../Downloads/A-small-attempt0.in')]
cases = int(inFile.pop(0))
rows = []

# set up test cases
for case in range(cases):
  answer = int(inFile.pop(0))
  rows.append(tuple(inFile[answer-1].split()))
  inFile = inFile[4:]
  answer = int(inFile.pop(0))
  rows.append(tuple(inFile[answer-1].split()))
  inFile = inFile[4:]

for i in range(0, len(rows), 2):
  count = 0
  magic = 0
  for num in rows[i]:
    if num in rows[i+1]:
      count += 1
      magic = int(num)

  if count == 0:
    print "Case #%d: Volunteer cheated!" % ((i+2)/2)
  elif count == 1:
    print "Case #%d: %d" % ((i+2)/2, magic)
  else:
    print "Case #%d: Bad magician!" % ((i+2)/2)

