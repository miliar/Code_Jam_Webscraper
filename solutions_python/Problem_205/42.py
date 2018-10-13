from Queue import Queue

T = int(raw_input())

for i in xrange(T):
    constants = map(int, raw_input().split())
    HD = constants[0]
    B = constants[4]
    D = constants[5]

    q = Queue()
    q.put((constants[0], constants[1], constants[2], constants[3], 0))
    past_states = set([])

    min_turn = -1

    while not q.empty():
        (hd, ad, hk, ak, t) = q.get()

        #print str((hd, ad, hk, ak, t))

        if (hd <= 0 or (hd, ad, hk, ak) in past_states):
            continue

        past_states.add((hd, ad, hk, ak))

        if (ad >= hk):
            min_turn = t + 1
            break

        q.put((hd - ak, ad, hk - ad, ak, t+1)) # atk
        q.put((HD - ak, ad, hk, ak, t+1)) # heal
        if (B > 0):
            q.put((hd - ak, ad + B, hk, ak, t+1)) # buff
        if (D > 0 and ak > 0):
            q.put((hd - (ak - D), ad, hk, ak - D, t+1)) # debuff

    if min_turn == -1:
        print "Case %d: IMPOSSIBLE" % (i + 1)

    else:
        print "Case %d: %d" % (i+1, min_turn)
