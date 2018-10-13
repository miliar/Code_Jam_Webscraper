T = int(raw_input())
for case in range(1,T+1):
    line = raw_input().split(" ")
    N = int(line.pop(0))
    S = int(line.pop(0))
    p = int(line.pop(0))
    scores = map(lambda x: int(x), line)
    ans = 0

    for score in scores:
        if (p-1) * 3 < score:
            # Even without 'using up' a surprise, the score fits
            # It could be p-1, p-1, p
            # If p is 0 then this is also ok, because any score also suffices
            ans = ans + 1
        elif p >= 2 and p * 3 - 4 <= score and S > 0:
            # The score could be p-2, p-2, p
            # If p = 1 then it must be the first case (no negative scores)
            S = S - 1
            ans = ans + 1
            

    print "Case #%d: %d" % (case, ans)
    
    
    
