

if __name__=="__main__":
    nCase = int(raw_input())
    for i in range(1, nCase+1):
        n,k = [int(v) for v in raw_input().split()]

        m = dict()
        m[n] = 1
        mk = n

        while k > 0:
            mk = max(m.keys())
            mv = m[mk]
            del m[mk]

            if mk/2 in m:
                m[mk/2] += mv
            else:
                m[mk/2] = mv 

            if (mk-1)/2 in m:
                m[(mk-1)/2] += mv
            else:
                m[(mk-1)/2] = mv

            k-= mv

        print "Case #{}: {} {}".format(i,(mk/2),(mk-1)/2)


