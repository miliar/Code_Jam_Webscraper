
def flip(ind, own, k):
    res = list(own)
    for i in xrange(ind, ind + k):
        if res[i] == "-":
            res[i] = "+"
        else:
            res[i] = "-"

    return "".join(res)



fin = open("input.txt", "r")

tests_num = int(fin.readline())

for i in xrange(tests_num):
    [own, k] = [x for x in fin.readline().split(" ")]
    #print own, int(k)
    ans = "".join(["+" for _ in xrange(len(own))])
    if own == ans:
        print "Case #" + str(i + 1) + ": " + str(0)
        continue
    k = int(k)
    q = [own]
    mp = {own: 0}
    l = 0
    r = 1
    while l < r:
        #print l
        #print "q[l] = ",  q[l]
        for ind in xrange(len(q[l]) - k +  1):
            new_own = flip(ind, q[l], k)
            #print new_own
            if not new_own in mp.keys():
                mp[new_own] = mp[q[l]] + 1
                q.append(new_own)
                r += 1
                if new_own == ans:
                    print "Case #" + str(i + 1) + ": " + str(mp[new_own])
                    l = r
                    break
        l += 1

    if not ans in mp.keys():
        print "Case #" + str(i + 1) + ": IMPOSSIBLE"


fin.close()