import sys
filein, fileout = sys.argv[1:3]

def solve(x,s,r,t,n,walkways):
    boost = {} # k: v <==> length v of k-speed walkway
    for b,e,w in walkways:
        boost[w] = boost.get(w,0) + (e-b)
    boost_length = sum(boost.values())
    if boost_length < x:
        boost[0] = x-boost_length

    time = 0
    for w, length in sorted(boost.items()):
        if t > 0:
            runtime = min(t,length/(r+w))
            walktime = (length-runtime*(r+w))/(s+w)
            time += runtime + walktime
            t -= runtime
        else:
            walktime = length/(s+w)
            time += walktime
    return '{:.9f}'.format(time)



if __name__ == '__main__':
    with open(filein, 'rU') as f1, open(fileout, 'w') as f2:
        T = int(f1.readline())
        for case in range(T):
            x,s,r,t,n = [int(x) for x in f1.readline().split()]
            walkways = []
            for i in range(n):
                b,e,w = [int(x) for x in f1.readline().split()]
                walkways.append((b,e,w))
            f2.write("Case #{}: {}\n".format(case+1, solve(x,s,r,t,n,walkways)))

