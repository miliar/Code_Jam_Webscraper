def main():
   row = input()
   for i in xrange(1, 5):
      r = raw_input().split()
      if i == row:
         selected1 = r
   row = input()
   for i in xrange(1, 5):
      r = raw_input().split()
      if i == row:
         selected2 = r
   results = set(selected1) & set(selected2)
   if len(results) == 0:
      return "Volunteer cheated!"
   if len(results) != 1:
      return "Bad magician!"
   return results.pop()


T = input()
for i in xrange(T):
   print "Case #%s: %s" % (i+1, main())
