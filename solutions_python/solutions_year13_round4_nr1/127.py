save = [0]
for i in range(200):
    save.append(save[-1]+i)

def solve(n,xs):
    ediscount = sum(save[e-b]*f for b,e,f in xs)
    ps = sorted(list(set([b for b,_,_ in xs]+[e for _,e,_ in xs])))
    bs = dict((p,sum(f for b,e,f in xs if b==p)) for p in ps)
    es = dict((p,sum(f for b,e,f in xs if e==p)) for p in ps)
    M=1000002013
    train = []
    adiscount = 0
    for p in ps:
        train.append((p,bs[p]))
        ex = es[p]
        while train:
            p0, n = train.pop()
            if n >= ex:
                adiscount += (save[p-p0]*ex) % M
                train.append((p0,n-ex))
                break
            else:
                adiscount += (save[p-p0]*n) % M
                ex-=n
    return (adiscount - ediscount)%M

rd=raw_input
for t in range(1,1+int(rd())):
    n,m=map(int,rd().split())
    print 'Case #%d: %d' % (t,solve(n,[map(int,rd().split()) for _ in range(m)]))

