test = int(raw_input())
for t in xrange(test):
   first = []
   kde = int(raw_input())
   
   for i in xrange(4):
      if i==kde-1:
         first=(raw_input().split(' '))
      else : lol = raw_input()
   second = []
   kde = int(raw_input())
   
   for i in xrange(4):
      if i==kde-1:
         second=(raw_input().split(' '))
      else : lol = raw_input()
  
   ans = [x for x in first if x in second]
   print "Case #%d: " %(t+1),
   if len(ans)==0:
      print "Volunteer cheated!"
   if len(ans)>1:
      print "Bad magician!"
   if len(ans)==1:
      print ans[0]
   
   
