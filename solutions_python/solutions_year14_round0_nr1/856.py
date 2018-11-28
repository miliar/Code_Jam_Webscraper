
"""
Input 
     
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
"""

from sys import stdin as fp

N = int(fp.readline())
for i in xrange(N):
    A1 = int(fp.readline())
    A1deck = []
    for j in range(4):
        A1deck.append(fp.readline().split())
        
    A2 = int(fp.readline())
    A2deck = []
    for j in range(4):
        A2deck.append(fp.readline().split())
    ans = set(A1deck[A1-1]) & set(A2deck[A2-1])
    if len(ans) == 1:
        print "Case #%s: %s" % (i+1, ans.pop())
    elif len(ans): 
        print "Case #%s: Bad magician!" % (i+1, )
    else:
        print "Case #%s: Volunteer cheated!" % (i+1, )        
