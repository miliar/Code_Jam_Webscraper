#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);
#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

const int maxN = 2000 + 100;

template<class T> bool lessT(const T &a, const T &b) { return a < b; }
template<> bool lessT(const double &a, const double &b) { return a < b - eps; }
template<class T> bool equalT(const T &a, const T &b) { return a == b; }
template<> bool equalT(const double &a, const double &b) { return fabs(a - b) < eps; }

template<typename T> struct costFlow {
  struct edge_t {
    int v, r, next; T w;
    edge_t(int v, int r, T w, int next) : v(v), r(r), w(w), next(next) { }
  };
  vector<edge_t> edges;
  int h[maxN], vis[maxN];
  T d[maxN];

  void clear() {
    edges.clear(); mset(h, -1);
  }

  void addE(int u, int v, int r, T w) {
    edges.push_back(edge_t(v, r, w, h[u]));
    h[u] = edges.size() - 1;
    edges.push_back(edge_t(u, 0, -w, h[v]));
    h[v] = edges.size() - 1;
  }

  void spfa(int s, int t, int n) {
    queue<int> q;
    fill(d + 1, d + 1 + n, numeric_limits<T>::max());
    fill(vis + 1, vis + 1 + n, false);
    d[s] = 0, q.push(s), vis[s] = true;
    while (!q.empty()) {
      int u = q.front();
      q.pop(), vis[u] = false;
      for (int i = h[u]; i != -1; i = edges[i].next) {
        const edge_t &e = edges[i];
        if (e.r && lessT(d[u] + e.w, d[e.v])) {
          d[e.v] = d[u] + e.w;
          if (!vis[e.v]) {
            q.push(e.v);
            vis[e.v] = true;
          }
        }
      }
    }
    for (int i = 1; i <= n; ++i) {
      if (i != t) d[i] = d[t] - d[i];
    }
    d[t] = 0;
  }

  int augment(int u, int t, int flow) {
    if (u == t) return flow;
    vis[u] = true;
    int ret = 0;
    for (int i = h[u]; i != -1; i = edges[i].next) {
      int v = edges[i].v, r = edges[i].r; T w = edges[i].w;
      if (r && !vis[v] && equalT(d[v] + w, d[u])) {
        int temp = augment(v, t, min(flow, r));
        if (temp) {
          edges[i].r -= temp, edges[i ^ 1].r += temp;
          ret += temp, flow -= temp;
          if (flow == 0) break;
        }
      }
    }
    return ret;
  }

  bool adjust(int n) {
    T delta = numeric_limits<T>::max();
    for (int u = 1; u <= n; ++u) {
      if (!vis[u]) continue;
      for (int i = h[u]; i != -1; i = edges[i].next) {
        const edge_t &e = edges[i];
        if (e.r && !vis[e.v] && lessT(d[u], d[e.v] + e.w)) {
          delta = min(delta, d[e.v] + e.w - d[u]);
        }
      }
    }
    if (delta == numeric_limits<T>::max()) return false;
    for (int i = 1; i <= n; ++i) {
      if (vis[i]) d[i] += delta;
    }
    mset0(vis);
    return true;
  }

  pair<int, T> minCostMaxFlow(int s, int t, int n) {
    int temp, flow = 0;
    T cost = 0;
    spfa(s, t, n);
    do {
      while ((temp = augment(s, t, maxint))) {
        flow += temp;
        mset0(vis);
      }
    } while (adjust(n));
    for (int i = 1; i < (int) edges.size(); i += 2) cost += edges[i].r * edges[i - 1].w;
    return make_pair(flow, cost);
  }
};

costFlow<int> cf;

int N, C, M, P[maxN], B[maxN];

int main() {
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    cf.clear();
    rd(N, C, M);
    int cnt1 = 0, cnt2 = 0;
    for (int i = 1; i <= M; ++i) {
      rd(P[i], B[i]);

      if (B[i] == 1) ++cnt1;
      else ++cnt2;
    }

    for (int i = 1; i <= M; ++i) {
      if (B[i] == 1) {
        cf.addE(M + 1, i, 1, 0);
      } else {
        cf.addE(i, M + 2, 1, 0);
      }
      for (int j = 1; j <= M; ++j) {
        if (i == j) continue;
        if (B[i] == B[j]) continue;
        if (B[i] == 2 || B[j] == 1) continue;
        if (P[i] == P[j]) {
          if (P[i] != 1) {
            cf.addE(i, j, 1, 1);
          }
        } else {
          cf.addE(i, j, 1, 0);
        }
      }
    }

    pair<int, int> f = cf.minCostMaxFlow(M + 1, M + 2, M + 2);
    int result = (min(cnt1, cnt2) - f.first) * 2 + f.first + max(cnt1, cnt2) - min(cnt1, cnt2);
    printf("Case #%d: %d %d\n", tt, result, f.second);
  }
  return 0;
}
