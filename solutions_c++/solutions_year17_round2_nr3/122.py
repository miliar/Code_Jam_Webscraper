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

const int maxN = 111;
int n, E[maxN], S[maxN];
int D[maxN][maxN];
LL g[maxN][maxN];
int q;

const LL maxLL = ~0ull >> 2;

double G[maxN][maxN];

void floyd1() {
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (D[i][j] != -1) {
        g[i][j] = D[i][j];
      } else {
        g[i][j] = maxLL;
      }
    }
    g[i][i] = 0;
  }
  for (int k = 1; k <= n; ++k) {
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
      }
    }
  }
}

void floyd2() {
  for (int k = 1; k <= n; ++k) {
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
      }
    }
  }
}

int main() {
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(n, q);
    for (int i = 1; i <= n; ++i) {
      rd(E[i], S[i]);
    }
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        rd(D[i][j]);
      }
    }
    floyd1();
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        if (g[i][j] <= E[i]) {
          G[i][j] = double(g[i][j]) / S[i];
        } else {
          G[i][j] = 1e50;
        }
      }
      G[i][i] = 0;
    }
    floyd2();
    printf("Case #%d: ", tt);
    for (int i = 1; i <= q; ++i) {
      int u, v;
      rd(u, v);
      printf("%.10f%c", G[u][v], i == q ? '\n' : ' ');
    }
  }
  return 0;
}
