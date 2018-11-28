#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

template<typename Ft> struct MaxFlow {
    static const int maxNodeCount = 5500;
    static const int maxEdgeCount = 33000 * 2;
    static const Ft feps = (Ft)1e-10, finf = (Ft)(1LL << 29);
    // graph
    int n, m;
    int lst[maxNodeCount];
    int nxt[maxEdgeCount], to[maxEdgeCount];
    Ft tof, cap[maxEdgeCount];
    int dst[maxNodeCount], srt[maxNodeCount], que[maxNodeCount], *qs, *qe, src, snk;
    //
    void init(int nodeCount) {
        n = nodeCount, m = 0, memset(lst, ~0, n << 2), tof = 0;
    }
    void add_edge(int u, int v, Ft fcap, Ft rcap = 0) {
        if (u == v) return;
        nxt[m] = lst[u], lst[u] = m, to[m] = v, cap[m] = fcap, m++;
        nxt[m] = lst[v], lst[v] = m, to[m] = u, cap[m] = rcap, m++;
    }
    Ft aug(int u, Ft flo) {
        if (u == snk) return flo;
        Ft df;
        for (int &e = srt[u]; ~e; e = nxt[e]) {
            if (cap[e] > feps && dst[u] < dst[to[e]]) {
                if ((df = aug(to[e], min(flo, cap[e]))) > feps) {
                    cap[e] -= df, cap[e ^ 1] += df;
                    return df;
                }
            }
        }
        return 0;
    }
    Ft dinic(int source, int sink, Ft flo_lim = finf) {
        int e, u, v;
        src = source, snk = sink;
        Ft df;
        for ( ; tof + feps < flo_lim; ) {
            qs = qe = que, memset(dst, ~0, n << 2);
            for (dst[*qe++ = src] = 0, srt[src] = lst[src]; qs != qe; ) {
                for (e = lst[u = *qs++]; ~e; e = nxt[e]) {
                    if (cap[e] > feps && !~dst[v = to[e]]) {
                        dst[*qe++ = v] = dst[u] + 1, srt[v] = lst[v];
                        if (v == snk) { qs = qe = 0; break; }
                    }
                }
            }
            if (!~dst[snk]) return tof;
            for (; (df = aug(src, flo_lim - tof)) > feps; ) tof += df;
        }
        return tof;
    }
};

MaxFlow<int> mf;

int n;
int p;
int reqs[60];
int min_ingr[60][60];
int max_ingr[60][60];

void solve_case() {
    n = getint(), p = getint();
    for (auto i = 0; i < n; ++i) reqs[i] = getint();
    for (auto i = 0; i < n; ++i) {
        const int c = reqs[i];
        for (auto j = 0; j < p; ++j) {
            const auto p = getint();
            max_ingr[i][j] = 10 * p / (9 * c);
            min_ingr[i][j] = (10 * p + 11 * c - 1) / (11 * c);
        }
    }
    mf.init(n * p + 2);
    for (auto i = 0; i < n - 1; ++i) {
        for (auto j1 = 0; j1 < p; ++j1) {
            for (auto j2 = 0; j2 < p; ++j2) {
                const auto min1 = min_ingr[i][j1];
                const auto max1 = max_ingr[i][j1];
                const auto min2 = min_ingr[i + 1][j2];
                const auto max2 = max_ingr[i + 1][j2];
                if (min1 > max1) continue;
                if (min2 > max2) continue;
                const auto min12 = max(min1, min2);
                const auto max12 = min(max1, max2);
                if (min12 <= max12) {
                    const auto k1 = i * p + j1;
                    const auto k2 = (i + 1) * p + j2;
                    mf.add_edge(k1, k2, 1);
                }
            }
        }
    }
    const auto s = n * p;
    const auto t = s + 1;
    for (auto j = 0; j < p; ++j) {
        if (min_ingr[0][j] <= max_ingr[0][j]) {
            mf.add_edge(s, j, 1);
        }
        if (min_ingr[n - 1][j] <= max_ingr[n - 1][j]) {
            mf.add_edge((n - 1) * p + j, t, 1);
        }
    }
    cout << mf.dinic(s, t) << endl;
    return;
}

int main () {
    const auto test_case = getint();
    for (auto test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
