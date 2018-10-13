#!/usr/bin/python


R, O, Y, G, B, V = range(6)
Str = "ROYGBV"

Lookup = dict(zip(Str, xrange(6)))


Map = [
   #[R, O, Y, G, B, V, ],
    [0, 0, 1, 1, 1, 0, ],
    [0, 0, 0, 0, 1, 0, ],
    [1, 0, 0, 0, 1, 1, ],
    [1, 0, 0, 0, 0, 0, ],
    [1, 1, 1, 0, 0, 0, ],
    [0, 0, 1, 0, 0, 0, ],
]

neigh = {}

neigh[R] = G
neigh[B] = O
neigh[Y] = V

def go(N, L):

    ret = ""
    curr = None

    import pdb
    #pdb.set_trace()

    for i in [R, B, Y]:
        if L[i]:
            curr = i
            L[i] -= 1
            ret += Str[i]
            N -= 1
            break

    while N:
        Max = 0
        Maxi = None
        for i in xrange(6):
            if Map[curr][i] and Max < L[i]:
                Maxi = i
                Max = L[i]

        if Maxi == None:
            #print ret
            return "IMPOSSIBLE"

        curr = Maxi
        L[Maxi] -= 1
        ret += Str[Maxi]
        N -= 1


    if not Map[Lookup[ret[0]]][Lookup[ret[-1]]] and len(ret) > 1:
        #print ret
        return "IMPOSSIBLE"

    return ret


def main():
    T = int(raw_input())
    for t in xrange(T):
        L = map(int, raw_input().split())
        N = L[0]
        L = L[1:]

        print "Case #%d: %s" % (
            t + 1,
            go(N, L),
        )
        
if __name__ == "__main__":
    main()
