#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < int(n); ++i)
#define REPE(i, a, b) for (int i = (a); i <= int(b); ++i)
#define SZ(x) ((int)(x).size())
#define ALL(x) x.begin(), x.end()
#define PB push_back
#define EB emplace_back
using LL = long long;
using PII = pair<int, int>;
#define F first
#define S second

int n, m, a[110], b[110][110], cur[110];

LL lb[110][110], ub[110][110];

LL lower(LL ing, LL price) {
  LL l = 0, r = 2e6;
  LL ans = r;
  while (l <= r) {
    LL m = (l + r) >> 1;
    if (price * m * 11 >= 10 * ing) ans = m, r = m - 1;
    else l = m + 1;
  }
  return ans;
}
LL upper(LL ing, LL price) {
  LL l = 0, r = 2e6;
  LL ans = 0;
  while (l <= r) {
    LL m = (l + r) >> 1;
    if (price * m * 9 <= 10 * ing) ans = m, l = m + 1;
    else r = m - 1;
  }
  return ans;
}

void solve() {
  scanf("%d%d", &n, &m);
  REP(i, n) scanf("%d", &a[i]);
  REP(i, n) REP(j, m) scanf("%d", &b[i][j]);
  REP(i, n) sort(b[i], b[i] + m);
  memset(cur, 0, sizeof cur);
  // puts("");
  REP(i, n) REP(j, m) {
    // printf("ing %d am %d: %lld - %lld\n", i, b[i][j], lower(b[i][j], a[i]), upper(b[i][j], a[i]));
    lb[i][j] = lower(b[i][j], a[i]);
    ub[i][j] = upper(b[i][j], a[i]);
  }
  int ans = 0;
  for (;;) {
    bool fg = false;
    REP(i, n) if (cur[i] >= m) fg = true;
    if (fg) break;
    LL l = 0, r = 2e6;
    REP(i, n) {
      int j = cur[i];
      l = max(l, lb[i][j]);
      r = min(r, ub[i][j]);
    }
    if (l <= r) {
      ans++;
      REP(i, n) cur[i]++;
    } else {
      REP(i, n) if (ub[i][cur[i]] == r) cur[i]++;
    }
  }
  printf("%d\n", ans);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int kase = 1; kase <= T; ++kase) {
    printf("Case #%d: ", kase);
    solve();
  }
  return 0;
}

