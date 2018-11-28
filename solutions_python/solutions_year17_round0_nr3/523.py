def split(x):
    s = x // 2
    return x - s, s

def solve(t):
    n,k = [int(x) for x in input().split()]

    if k == 1:
        return split(n-1)

    k -= 1
    mx,mn = split(n-1)
    if mx != mn:
        current = [(mx,1),(mn,1)]
    else:
        current = [(mx,2)]
    a = 2

    #print(current)
    while k > a:
        nx = {}

        for s,c in current:
            sx,sn = split(s-1)

            if sx not in nx:
                nx[sx] = 0
            nx[sx] += c

            if sn not in nx:
                nx[sn] = 0
            nx[sn] += c

        current = []
        values = sorted(nx.keys())
        values.reverse()
        for v in values:
            current.append((v,nx[v]))

        #print(current)
        k -= a
        a *= 2

    if k <= current[0][1]:
        return split(current[0][0]-1)
    else:
        return split(current[1][0]-1)

def main():
    t = int(input())
    for tt in range(t):
        mx,mn = solve(tt+1)
        print("Case #%d: %d %d" % (tt+1,mx,mn))

if __name__=='__main__':
    main()

    
