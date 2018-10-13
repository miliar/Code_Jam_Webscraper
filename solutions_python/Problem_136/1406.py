import sys

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    # print "---------------------"
    k = sys.stdin.readline().split()
    C = float(k[0])
    F = float(k[1])
    X = float(k[2])
        
    # print "X=", X
    a = [2.0]
    b = [0.0]
    minX = X/2
    i = 0

    while (True):
        i += 1
        # print i
        # print "i=", i
        a.append(2.0 + i*F)
        b.append(a[i]*(b[i-1]-C)/a[i-1])
        # print "a=", a[i]
        # print "b=", b[i]

        aaa = (X-b[i])/a[i]
        # print "krysser y=C naar x = ", aaa
        # print "krysser y=0 naar x = ", -b[i]/a[i]
        if aaa < minX:
            minX = aaa
        else:
            break

        # j = i+1
        # a2 = 2 + j*F
        # v2 = (2+(j+1)*F)/(2+j*F)
        # w2 = -C*v2
        # b2 = w2*(v2**j - 1)/(v2-1)
        # print "a2 = ", a2
        # print "b2 = ", b2

    print "Case #" + str(tc) + ":",
    print("%.7f" % minX)







