import sys
for TT in range(1, input()+1):
    N = input()
    transmap = {'_cnt': 0}

    def trans(w):
        if w not in transmap:
            cnt = transmap['_cnt']
            cnt += 1
            transmap['_cnt'] = cnt
            transmap[w] = cnt
        return transmap[w]

    eng = map(trans, raw_input().split())
    fr = map(trans, raw_input().split())

    words = []
    for i in range(N-2):
        words.append(map(trans, raw_input().split()))

    ans = 9999999
    chkorig = [0] * (transmap['_cnt']+1)
    for w in eng:
        chkorig[w] |= 1
    for w in fr:
        chkorig[w] |= 2

    for i in range(0, 2**(N-2)):
        bit = 1
        cnt = 0

        chk = chkorig[:]
        for word in words:
            if i & bit:
                status = 1
            else:
                status = 2
            bit <<= 1

            for w in word:
                chk[w] |= status

        for elem in chk:
            if elem == 3:
                cnt += 1

        ans = min(ans, cnt)

    print "Case #{}: {}".format(TT, ans)
    print >>sys.stderr, TT
