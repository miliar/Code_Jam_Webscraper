for c in range(1,input()+1):
    x = map(int,raw_input().split())

    n = x[0]
    s = x[1]
    p = x[2]
    ti = x[3:]


    count = 0
    surcount = 0

    for t in ti:

        q,r = divmod(t,3)

        if p == 0:
               count += 1

        elif p == 1:
            if t > 0:
                count += 1

        else:
            if (p-1 == q and r == 0) or (p-2 == q and r == 2):
                if surcount < s:
                    surcount += 1
                    count += 1

            elif q + r < p:
                pass

            else:
                count += 1

    print"Case #%d:"%c, count
