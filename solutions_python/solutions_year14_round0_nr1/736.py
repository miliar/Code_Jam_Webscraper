for t in xrange(input()):
 r = input()
 a = [ map(int,raw_input().split()) for i in xrange(4) ][r-1]
 r = input()
 b = [ map(int,raw_input().split()) for i in xrange(4) ][r-1]
 ans = list(set(a).intersection(set(b)))
 #print ans
 print "Case #%d:"%(t+1),
 if len(ans) ==1: print ans[0]
 elif len(ans) >1 : print "Bad magician!"
 else: print "Volunteer cheated!"
 