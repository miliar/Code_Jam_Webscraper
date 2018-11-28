#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        n, q = [int(jk) for jk in raw_input().split()]
        e = []
        s = []
        for _ in range(n):
            ei, si = [int(jk) for jk in raw_input().split()]
            e.append(ei)
            s.append(si)

        d = []
        for i in range(n):
            dr = [1000000000000.0 if jk == '-1' else int(jk) for jk in raw_input().split()]
            d.append(dr)

        # floyd warshall distances
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        G = [[1000000000000.0 for _ in range(n)] for __ in range(n)]
        for i, (ei, si) in enumerate(zip(e, s)):
            for j, dij in enumerate(d[i]):
                if dij <= ei:
                    G[i][j] = dij / (1.0*si)

        #print G
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])

        # queries
        for _ in range(q):
            u, v = [int(jk) for jk in raw_input().split()]
            print G[u-1][v-1],

        print


if __name__ == '__main__':
    main()
