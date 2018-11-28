#include <cstdio>
#include <cstring>
#include <algorithm>

const int N = 100 + 10;

inline void check(int &lhs, int rhs) { lhs = (lhs > rhs ? lhs : rhs); }

int n, m, g[N], f[N][N][N];

void init() {
  memset(f, 0, sizeof f);
  f[0][0][0] = 0;
  for (int i = 0; i <= 100; ++i) {
    for (int j = 0; j <= 100; ++j) {
      for (int k = 0; k <= 100; ++k) {
        if (i || j || k) check(f[i][j][k], 1);
        int cur = f[i][j][k] + 1;
        check(f[i + 1][j][k + 1], cur);
        check(f[i][j + 2][k], cur);
        check(f[i + 4][j][k], cur);
        check(f[i][j][k + 4], cur);
        check(f[i + 2][j + 1][k], cur);
        check(f[i][j + 1][k + 2], cur);
      }
    }
  }
}

int main() {
  init();
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i) scanf("%d", &g[i]);
    int cnt[4];
    memset(cnt, 0, sizeof cnt);
    for (int i = 1; i <= n; ++i) ++cnt[g[i] % m];
    int ans = cnt[0];
    if (m == 2) {
      ans += (cnt[1] + 1) / 2;
    } else if (m == 3) {
      int x = std::min(cnt[1], cnt[2]);
      cnt[1] -= x, cnt[2] -= x, ans += x;
      ans += (cnt[1] + 2) / 3 + (cnt[2] + 2) / 3;
    } else {
      ans += f[cnt[1]][cnt[2]][cnt[3]];
    }
    printf("Case #%d: %d\n", tid, ans);
  }
  return 0;
}
