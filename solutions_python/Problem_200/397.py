T = int(raw_input())

def poss(l, beg, N):
    rem = l - len(beg)
    return int(beg + beg[-1] * rem) <= N

for t in xrange(T):
    N = int(raw_input())

    ans = 1
    for l in xrange(1, 20):
       last = 1
       tmp = ""
       for _ in xrange(l):
           for attempt in xrange(9, 0, -1):
               if attempt < last: break
               if poss(l, tmp + str(attempt), N):
                   tmp += str(attempt)
                   last = attempt
                   break

           if len(tmp) != _ + 1:
               break
       if len(tmp) == l:
           ans = max(ans, int(tmp))
    print "Case #%d: %d" % (t + 1, ans)

