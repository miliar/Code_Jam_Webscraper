
from datetime import datetime

def getNWins(n, k):
    tmp_n = sorted(n)
    tmp_k = sorted(k)
    nw    = 0
    for cn in tmp_n[::-1]:
        mik = min(tmp_k)
        mak = max(tmp_k)
        if cn > mak:
            nw += 1
            tmp_k.remove(mik)
        else:
            tmp_k.remove(min([val for val in tmp_k if val > cn]))
    return nw


def getDWins(n, k):
    tmp_n = sorted(n)
    tmp_k = sorted(k)
    nw    = 0
    while len(tmp_n) > 0:
        min_n = tmp_n.pop(0)
        min_k = min(tmp_k)
        max_k = max(tmp_k)
        if min_n < min_k:
            tmp_k.remove(max_k)
        elif min_n > max_k:
            nw += (len(tmp_n)+1)
            tmp_n = []
        else:
            nw += 1
            tmp_k.remove(min_k)
    return nw

if __name__ == "__main__":
    fin = "../in/large.in"
    fou = "../out/large.out"

    stt = datetime.now()

    inf = open(fin,"r")
    ouf = open(fou,"w")

    cases = int(inf.readline())
    for t in range(cases):
        n = int(inf.readline())
        naomi = map(float, inf.readline().split())
        ken   = map(float, inf.readline().split())
        nwins = getNWins(naomi, ken)
        dwins = getDWins(naomi, ken)
        ouf.write("Case #%d: %d %d\n" % ((t+1), dwins, nwins))

    inf.close()
    ouf.close()

    print "Answer in: " + str(datetime.now() - stt)
