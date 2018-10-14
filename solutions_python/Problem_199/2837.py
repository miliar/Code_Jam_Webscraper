t = int(raw_input())

for i in xrange(1, t+1):
    p1, n = raw_input().split(' ')
    n = int(n)
    pan = []
    for p in p1:
        pan.append(p)
    #print pan, n
    count = 0

    for j in range(len(pan)):
        if (pan[j] == "-" and j + n > len(pan)):
            count = -1
            break
        elif (pan[j] == "-"):
            #print "Flipping"
            count += 1
            for k in xrange(j, j+n):
                if(pan[k] == "-"):
                    pan[k] = "+"
                elif (pan[k] == "+"):
                    pan[k] = "-"

    #print "Answer: ", count
    if (count < 0):
        count = "IMPOSSIBLE"

    print('Case #{0}: {1}'.format(i, count))
