# t1, t2,t3,t4 = map(raw_input().split(' '), int)
# print (t1 + t2)

mt = [[],[],[],[]]

nro = int(raw_input())
for x in range(0,(nro)):

    item1 = int(raw_input()) - 1
    linen1 = []

    for i in range(0,4):
        a =  map(int, raw_input().split(" "))
        mt[i] = a

    linen1 = mt[item1]

    item2 = int(raw_input()) - 1
    linen2 = []
    for i in range(0,4):
        b =  map(int, raw_input().split(" "))
        mt[i] = b

    linen2 = mt[item2]

    cnt = 0
    resp_nro = 0

    for m in linen1:
        # import ipdb; ipdb.set_trace()
        if linen2.count(m) > 0:
            cnt = cnt + 1
            resp_nro = m

    resp = ""

    if cnt == 0:
        print "Case #%i: Volunteer cheated!" % (x+1)
    elif cnt == 1:
        print "Case #%i: %i" % (x+1, resp_nro)
    elif cnt > 1:
        print "Case #%i: Bad magician!" % (x+1)

