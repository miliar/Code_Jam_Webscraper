#include <bits/stdc++.h>

const int N = 5e3, M = N * 20;
int cc, S, T;
int adj[N], v[M], f[M], c[M], nxt[M], e;
__inline void ins(int u0, int v0, int f0, int c0) {
    v[e] = v0; f[e] = f0; c[e] =  c0; nxt[e] = adj[u0]; adj[u0] = e ++;
    v[e] = u0; f[e] =  0; c[e] = -c0; nxt[e] = adj[v0]; adj[v0] = e ++;
}

int Q[65536];
bool inQ[N];
int d[N], p[N], pe[N];
int SPFA() {
    memset(d, -1, sizeof(*d) * cc);
    d[S] = 0;
    unsigned short l = 0, r = 0;
    Q[r ++] = S; inQ[S] = true;
    while (l != r) {
        int u = Q[l ++]; inQ[u] = false;
        for (int e = adj[u]; ~e; e = nxt[e])
            if (f[e]) {
                if (!~d[v[e]] || d[v[e]] > d[u] + c[e]) {
                    d[v[e]] = d[u] + c[e];
                    p[v[e]] = u;
                    pe[v[e]] = e;
                    if (!inQ[v[e]]) {
                        Q[r ++] = v[e];
                        inQ[v[e]] = true;
                    }
                }
            }
    }
    return d[T];
}

std::pair<int, int> flow() {
    int maxflow = 0, cost = 0;
    while (~SPFA()) {
        int tmp = 1e9;
        for (int u = T; u != S; u = p[u]) tmp = std::min(tmp, f[pe[u]]);
        maxflow += tmp;
//        std::cout << tmp << std::endl;
        for (int u = T; u != S; u = p[u]) {
            f[pe[u]] -= tmp;
            f[pe[u] ^ 1] += tmp;
            cost += tmp * c[pe[u]];
        }
    }
    return std::make_pair(maxflow, cost);
}

int A[N], AA[N], B[N], toT[N], cnt[N];

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int TT; std::cin >> TT;
    for (int ca = 1; ca <= TT; ++ ca) {
        memset(adj, -1, sizeof adj); cc = 0; e = 0;
        S = cc ++; T = cc ++;
        int n, c, m; std::cin >> n >> c >> m;
        for (int i = 1; i <= n; ++ i) {
            A[i] = cc ++; AA[i] = cc ++;
            toT[i] = e;
            ins(AA[i], T, 0, 0);
            ins(A[i], AA[i], 1e9, 0);
            if (i > 1) ins(A[i], A[i - 1], 1e9, 0);
        }

        for (int i = 1; i <= c; ++ i) {
//            B[i] = cc ++;
//            ins(S, B[i], 1, 0);
            cnt[i] = 0;
        }

        for (int i = 1; i <= m; ++ i) {
            int p, b; std::cin >> p >> b;
            ++ cnt[b];
            B[i] = cc ++;
            ins(S, B[i], 1, 0);
            ins(B[i], AA[p], 1, 0);
            if (p > 1) ins(B[i], A[p - 1], 1, 1);
        }

        int l = 0, r = m;
        for (int i = 1; i <= c; ++ i)
            if (cnt[i] - 1 > l) l = cnt[i] - 1;

        while (l < r - 1) {
            int mid = (l + r) / 2;
            for (int i = 0; i < e; i += 2) {
                f[i] += f[i ^ 1];
                f[i ^ 1] = 0;
            }
            for (int i = 1; i <= n; ++ i)
                f[toT[i]] = mid;

            auto res = flow();
//            std::cout << l << " " << r << " " << res.first << " " << res.second << std::endl;
            if (res.first < m) l = mid; else r = mid;
        }
  //      std::cout << r << std::endl;

        for (int i = 0; i < e; i += 2) {
            f[i] += f[i ^ 1];
            f[i ^ 1] = 0;
        }
        for (int i = 1; i <= n; ++ i)
            f[toT[i]] = r;

        auto res = flow();
        std::cout << "Case #" << ca << ": " << r << " " << res.second << std::endl;
    }
}
