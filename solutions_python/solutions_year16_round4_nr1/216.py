import string
from operator import itemgetter



def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine



def sortpair(pair):
    n = len(pair)/2
    l = pair[:n]
    r = pair[n:]
    #if n > 1:
        #print l, r, l > r

    if l > r:
        return r+l
    return pair

def main():
    T = int( raw_input() )

    for t in xrange(T):    
        N,R,P,S = map(int, raw_input().split())
        total = R+P+S

        l = ''
        if N == 1:
            l = P*'P' + 'R'*R + 'S'*S
            if l[0] == l[1]:
                output(t, None)
            else:
                output(t, l)
            continue

        if P > R+S or R > P+S or S>P+R:
            output(t, None)
            continue
        if P == 0 or R == 0 or S == 0:
            output(t, None)
            continue

        players = [['P', P], ['R',R], ['S',S]]
        players.sort(key = itemgetter(1), reverse = True)
        d = total / 3
        r = total - 3*d
        if players[2][1] != d or players[0][1] != d+1 or players[1][1] != d + (r==2):
            output(t, None)
            continue


        pairs2 = players[0][1] / 2
        pairs1 = players[0][1] - pairs2
        pairs = []
        key = sortpair(players[0][0] + players[1][0])
        pairs.append([key, pairs1])
        key = sortpair(players[0][0] + players[2][0])
        pairs.append([key, pairs2])
        key = sortpair(players[1][0] + players[2][0])
        pairs.append([key, players[1][1]-pairs1])

        l = ''
        for i in xrange(total/2):
            i1 = i % 3
            if (pairs[i1][1] > 0):
                l += pairs[i1][0]
                pairs[i1][1] -= 1

        for j in xrange(2,N):
            blocksize = 2**j
            for i in xrange(total/blocksize):
                l = l[:i*blocksize] + sortpair(l[i*blocksize:(i+1)*blocksize]) + l[(i+1)*blocksize:]
        output(t, l)


if __name__ == "__main__":
   main()