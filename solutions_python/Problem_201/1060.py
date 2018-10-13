
T = input()

for case in xrange(1,T+1):
    n,k = [int(i) for i in raw_input().split()]
    
    k = k - 1

    t = 1

    hole = {n:1}
    
    while k > 0:
        if k >= t:
            newhole = {}
            for h in hole:
                if h % 2 == 1:
                    newhole[h/2] = newhole.get(h/2,0) + 2 * hole[h]

                else:
                    newhole[h/2] = newhole.get(h/2,0) +  hole[h]
                    newhole[(h-1)/2] = newhole.get((h-1)/2,0) +  hole[h]

                    
            hole = newhole
            
            k -= t
            t *= 2

        else:
            h = hole.keys()
            if len(h) == 1:
                ans = h[0]
                break

            else:
                h1 = max(h)
                h2 = min(h)
                #print hole,k
                if hole[h1] > k:
                    ans = h1
                    break
                else:
                    ans = h2
                    break
                



    else:
        ans = max(hole.keys())
        
    if ans % 2 == 0:
        ans = str(ans/2) + " " + str((ans-1)/2)
    else:
        ans = str(ans/2) + " " + str(ans/2)

    print "Case #%d: %s" % (case,ans)

