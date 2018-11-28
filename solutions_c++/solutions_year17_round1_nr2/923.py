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

const int maxN = 55;
int n, P, R[maxN], Q[maxN][maxN];
int l[maxN][maxN], r[maxN][maxN];

struct item_t {
  int l, r;
  bool operator<(const item_t &x) const {
    return l < x.l;
  }
  item_t(int x, int y) {
    l = x; r = y;
  }
};
multiset<item_t> S[maxN];
int cnt[maxN];

struct interval_t {
  int l, r, index;
  bool operator<(const interval_t &x) const {
    if (r != x.r) {
      return r > x.r;
    }
    return l > x.l;
  }
  interval_t(int x, int y, int z) {
    l = x, r = y, index = z;
  }
};

int solve() {
  vector<interval_t> vv;

  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= P; ++j) {
      int x = Q[i][j] * 10;
      int y = (R[i] * 11);
      l[i][j] = x / y;
      if (x % y != 0) {
        ++l[i][j];
      }
      r[i][j] = Q[i][j] * 10 / (R[i] * 9);
      if (l[i][j] > 0 && l[i][j] <= r[i][j]) {
        vv.push_back(interval_t(l[i][j], r[i][j], i));
      }
    }
  }
  sort(vv.begin(), vv.end());

  for (int i = 1; i <= n; ++i) {
    S[i].clear();
  }
  memset(cnt, 0, sizeof(cnt));
  int total = 0;
  int ret = 0;

  for (int i = 0; i < vv.size(); ++i) {
    int curr = vv[i].r;
    for (int j = 1; j <= n; ++j) {
      while (!S[j].empty() && S[j].begin()->l > curr) {
        S[j].erase(S[j].begin());
        --cnt[j];
        if (cnt[j] == 0) {
          --total;
        }
      }
    }
    S[vv[i].index].insert(item_t(vv[i].l, vv[i].r));
    ++cnt[vv[i].index];
    if (cnt[vv[i].index] == 1) {
      ++total;
    }

    while (total == n) {
      for (int j = 1; j <= n; ++j) {
        assert(!S[j].empty());
        S[j].erase(S[j].begin());
        --cnt[j];
        if (cnt[j] == 0) {
          --total;
        }
      }
      ++ret;
    }
  }
  return ret;
}

int main() {
  freopen("B-small-attempt1.in", "r", stdin);

  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(n, P);
    for (int i = 1; i <= n; ++i) {
      rd(R[i]);
    }
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= P; ++j) {
        rd(Q[i][j]);
      }
    }
    printf("Case #%d: %d\n", tt, solve());
  }
  return 0;
}
