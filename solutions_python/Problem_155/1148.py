cases = int(raw_input())

for case in range(cases):
    smax, sstr = raw_input().split()
    smax = int(smax)
    slevel = 0
    total_people = int(sstr[slevel])
    slevel = 1
    added = 0
    while slevel <= smax:
        if total_people < slevel:
            toadd = (slevel - total_people)
            added += toadd
            total_people += toadd
        total_people += int(sstr[slevel])
        if(total_people >= smax):
            break
        slevel += 1
    print "Case #{}: {}".format(case+1, added)


         