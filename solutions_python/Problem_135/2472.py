def read_chosen_line():
  row_chosen = int(input())
  result = set([])
  for row in range(1, 4 + 1):
    if row_chosen == row:
      result = set(raw_input().split())
    else:
      raw_input() # skip line
  return result


cases = input()
for case in xrange(1, cases + 1):
  intersect = read_chosen_line() & read_chosen_line()
  if len(intersect) > 1:
    print "Case #%d: Bad magician!" % case
  if len(intersect) == 0:
    print "Case #%d: Volunteer cheated!" % case
  if len(intersect) == 1:
    print "Case #%d: %s" % (case, intersect.pop())
