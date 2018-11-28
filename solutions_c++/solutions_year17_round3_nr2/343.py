#include <cstdio>
#include <cstring>
#include <algorithm>

inline void check(int &lhs, int rhs) { lhs = (lhs < rhs ? lhs : rhs); }

const int N = 24 * 60;

int tag[N];

int solve(int s) {
  static int f[N + 1][N + 1][2];
  memset(f, 0x3f, sizeof f);
  f[0][0][s] = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j <= N; ++j) {
      for (int k = 0; k < 2; ++k) {
        int cur = f[i][j][k];
        if (tag[i] != k) {
          check(f[i + 1][j + k][k], cur);
          check(f[i + 1][j + k][!k], cur + 1);
        }
      }
    }
  }
  return std::min(f[N][N / 2][s], f[N][N / 2][!s] + 1);
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    int n, m;
    scanf("%d%d", &n, &m);
    memset(tag, -1, sizeof tag);
    for (int i = n; i--;) {
      int l, r;
      scanf("%d%d", &l, &r);
      std::fill(tag + l, tag + r, 0);
    }
    for (int i = m; i--;) {
      int l, r;
      scanf("%d%d", &l, &r);
      std::fill(tag + l, tag + r, 1);
    }
    printf("Case #%d: %d\n", tid, std::min(solve(0), solve(1)));
  }
  return 0;
}
