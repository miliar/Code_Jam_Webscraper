import sys
'''
'''


if __name__  == '__main__':

    xx = sys.stdin.readline()
    num = 0
    for line in sys.stdin:
        num += 1
        (n, k) = line.strip().split()
        n = int(n)
        k = int(k)

        # instead of keeping full set of numbers, keep count of each number, move in chunks until K
        cnt = {}
        cnt[n] = 1
        i = 0
        while i<k:
            pick = sorted(cnt,reverse=True)[0] # biggest one
            rep = cnt[pick] # do this many at once
            # process all p's into children at once
            for x in pick/2,(pick-1)/2:
                if x not in cnt:
                    cnt[x] = 0
                cnt[x] += rep
            res = (pick/2,(pick-1)/2)
            del(cnt[pick])
            i += rep
        #print res
        print 'Case #'+str(num)+': '+ str(res[0])+' '+str(res[1])
