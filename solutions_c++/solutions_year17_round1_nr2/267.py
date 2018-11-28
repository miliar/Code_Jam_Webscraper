#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const int M = 1e6, N = M, inf = 0x3f3f3f3f;
int last[N], dist[N], cur[N], q[N];
int ff[4 * M], pred[4 * M];
int cap[4 * M];

void clr()
{
    memset(last, 0, sizeof(last));
    memset(dist, 0, sizeof(dist));
    memset(cur, 0, sizeof(cur));
    memset(q, 0, sizeof(q));
    memset(ff, 0, sizeof(ff));
    memset(pred, 0, sizeof(pred));
    memset(cap, 0, sizeof(cap));
}

struct dinic
{
    int n, m;
    dinic(int nv)
    {
        n = nv, m = 0;
        for (int i = 0; i < n; i++) last[i] = -1;
    }
    void add(int x, int y, int c)
    {
        ff[m] = y, cap[m] = c, pred[m] = last[x], last[x] = m++;
        ff[m] = x, cap[m] = 0, pred[m] = last[y], last[y] = m++;
    }
    int push(int u, int sink, int flow)
    {
        if (u == sink) return flow;
        for (int& e = cur[u]; e >= 0; e = pred[e])
        {
            int v = ff[e];
            if (cap[e] > 0 and dist[u] + 1 == dist[v])
                if (int aug = push(v, sink, min(flow, cap[e])))
                    return cap[e] -= aug, cap[e^1] += aug, aug;
        }
        return 0;
    }
    int flow(int source, int sink)
    {
        int ret = 0;
        while (true)
        {
            for (int i = 0; i < n; i++) cur[i] = last[i], dist[i] = -1;

            int qs = 0, qe = 0;
            q[qe++] = source;
            dist[source] = 0;
            while (qs < qe)
            {
                int u = q[qs++];
                for (int e = last[u]; e >= 0; e = pred[e])
                {
                    int v = ff[e];
                    if (cap[e] > 0 and dist[v] < 0)
                        q[qe++] = v, dist[v] = dist[u] + 1;
                }
            }
            if (dist[sink] < 0) break;
            while (int aug = push(source, sink, inf)) ret += aug;
        }
        return ret;
    }
};
int r[55], Q[55][55];

inline int up(int a, int b)
{
    return (a + b - 1) / b;
}

inline int dn(int a, int b)
{
    return a / b;
}

bool good(int a, int b, int r1, int r2)
{
    int lo = -100, hi = inf;
    lo = max(lo, up(10 * a, 11 * r1));
    lo = max(lo, up(10 * b, 11 * r2));
    hi = min(hi, dn(10 * a, 9 * r1));
    hi = min(hi, dn(10 * b, 9 * r2));
    if (lo > hi or hi == 0)
        return false;
    return true;
}

#undef int
int main()
{
#define int long long
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        clr();
        int n, p; cin >> n >> p;
        for (int i = 1; i <= n; i++)
            cin >> r[i];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= p; j++)
                cin >> Q[i][j];

        int source = 0, sink = n * p + (n - 1) * p + 1;
        dinic fl(sink + 1);
        for (int j = 1; j <= p; j++)
        {
            fl.add(source, j, 1);
            {
                int lo = -100, hi = inf;
                lo = max(lo, up(10 * Q[n][j], 11 * r[n]));
                hi = min(hi, dn(10 * Q[n][j], 9 * r[n]));
                if (lo <= hi and hi > 0)
                    fl.add((n - 1) * p + j, sink, 1);
            }
        }
        for (int i = 0; i <= n - 2; i++)
            for (int j = 1; j <= p; j++)
            {
                int cur = i * p + j;
                int lo = -100, hi = inf;
                lo = max(lo, up(10 * Q[i + 1][j], 11 * r[i + 1]));
                hi = min(hi, dn(10 * Q[i + 1][j], 9 * r[i + 1]));
                if (lo <= hi and hi > 0)
                    fl.add(cur, cur + n * p, 1);
            }

        for (int i = 0; i <= n - 2; i++)
            for (int j = 1; j <= p; j++)
                for (int nxt_j = 1; nxt_j <= p; nxt_j++)
                {
                    int src = n * p + (i * p + j);
                    int dst = (i + 1) * p + nxt_j;
                    int fst = Q[i + 1][j], snd = Q[i + 2][nxt_j];
                    if (good(fst, snd, r[i + 1], r[i + 2]))
                        fl.add(src, dst, 1);
                }
        cout << "Case #" << tt << ": " << fl.flow(source, sink) << "\n";
    }
    return 0;
}
