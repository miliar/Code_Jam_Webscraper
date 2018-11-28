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
int n, m;
char mp[maxN][maxN];

void solve() {
  for (int i = 2; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      if (mp[i][j] == '?') {
        mp[i][j] = mp[i-1][j];
      }
    }
  }
  for (int i = n - 1; i >= 1; --i) {
    for (int j = 1; j <= m; ++j) {
      if (mp[i][j] == '?') {
        mp[i][j] = mp[i+1][j];
      }
    }
  }
  for (int j = 2; j <= m; ++j) {
    for (int i = 1; i <= n; ++i) {
      if (mp[i][j] == '?') {
        mp[i][j] = mp[i][j-1];
      }
    }
  }
  for (int j = m-1; j >= 1; --j) {
    for (int i = 1; i <= n; ++i) {
      if (mp[i][j] == '?') {
        mp[i][j] = mp[i][j+1];
      }
    }
  }
}

int main() {
  freopen("A-large.in", "r", stdin);
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    scanf("%d%d\n", &n, &m);
    for (int i = 1; i <= n; ++i) {
      scanf("%s", mp[i]+1);
    }
    solve();
    printf("Case #%d:\n", tt);
    for (int i = 1; i <= n; ++i) {
      printf("%s\n", mp[i]+1);
    }
  }
  return 0;
}
