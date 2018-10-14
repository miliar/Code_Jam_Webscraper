import sys

def max_not_surprising(t):
    max_score = t / 3
    if t > 0 and t % 3 > 0: 
        max_score += 1

    return min(max_score, 10)     
       
def max_surprising(t):
    max_score = t / 3
    if t > 0:
      if t % 3 == 2:
          max_score += 2
      else:
          max_score += 1 

    return min(max_score, 10)    

numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    elems = [int(x) for x in sys.stdin.readline().rstrip("\r\n").split(" ")]

    googlers    = elems[0]
    surprises   = elems[1]
    p           = elems[2]
    googler_scores = elems[3:]
    m = 0
    for googler_score in googler_scores:
        if max_not_surprising(googler_score) >= p:
            m += 1
        else:
            if surprises > 0 and max_surprising(googler_score) >= p:
                m += 1
                surprises -= 1

    print "Case #%d: %u" % (casenumber, m)

