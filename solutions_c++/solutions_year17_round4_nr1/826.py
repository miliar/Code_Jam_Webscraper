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

const int maxN = 102;
int tests, n, P, G[maxN];
int dp2[2][maxN];
int dp3[3][maxN][maxN];
int dp4[4][maxN][maxN][maxN];
int cnt[4];

void update(int& x, int v) {
  x = min(x, v);
}

int solve2() {
  dp2[0][0] = 0;
  for (int i = 0; i <= cnt[1]; ++i)  {
    for (int ch = 0; ch < P; ++ch) {
      if (dp2[ch][i] == maxint) {
        continue;
      }
      update(dp2[(ch + 1) % P][i + 1], dp2[ch][i] + (ch == 0 ? 0 : 1));
    }
  }
  int ret = maxint;
  for (int ch = 0; ch < P; ++ch) {
    ret = min(ret, dp2[ch][cnt[1]]);
  }
  return ret;
}

int solve3() {
  dp3[0][0][0] = 0;
  for (int i = 0; i <= cnt[1]; ++i)  {
    for (int j = 0; j <= cnt[2]; ++j) {
      for (int ch = 0; ch < P; ++ch) {
        if (dp3[ch][i][j] == maxint) {
          continue;
        }
        update(dp3[(ch + 1) % P][i + 1][j], dp3[ch][i][j] + (ch == 0 ? 0 : 1));
        update(dp3[(ch + 2) % P][i][j + 1], dp3[ch][i][j] + (ch == 0 ? 0 : 1));
      }
    }
  }
  int ret = maxint;
  for (int ch = 0; ch < P; ++ch) {
    ret = min(ret, dp3[ch][cnt[1]][cnt[2]]);
  }
  return ret;
}

int solve4() {
  dp4[0][0][0][0] = 0;
  for (int i = 0; i <= cnt[1]; ++i)  {
    for (int j = 0; j <= cnt[2]; ++j) {
      for (int k = 0; k <= cnt[3]; ++k) {
        for (int ch = 0; ch < P; ++ch) {
          if (dp4[ch][i][j][k] == maxint) {
            continue;
          }
          update(dp4[(ch + 1) % P][i + 1][j][k], dp4[ch][i][j][k] + (ch == 0 ? 0 : 1));
          update(dp4[(ch + 2) % P][i][j + 1][k], dp4[ch][i][j][k] + (ch == 0 ? 0 : 1));
          update(dp4[(ch + 3) % P][i][j][k + 1], dp4[ch][i][j][k] + (ch == 0 ? 0 : 1));
        }
      }
    }
  }
  int ret = maxint;
  for (int ch = 0; ch < P; ++ch) {
    ret = min(ret, dp4[ch][cnt[1]][cnt[2]][cnt[3]]);
  }
  return ret;
}

int main() {
  freopen("A-large.in", "r", stdin);
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(n, P);
    memset(cnt, 0, sizeof(cnt));
    for (int i = 1; i <= n; ++i) {
      rd(G[i]);
      G[i] %= P;
      ++cnt[G[i]];
    }
    memset(dp2, 0x7f, sizeof(dp2));
    memset(dp3, 0x7f, sizeof(dp3));
    memset(dp4, 0x7f, sizeof(dp4));

    int ret = 0;
    if (P == 2) {
      ret = solve2();
    } else if (P == 3) {
      ret = solve3();
    } else {
      ret = solve4();
    }
    ret = n - ret;
    printf("Case #%d: %d\n", tt, ret);
  }
  return 0;
}
