#include <cstdio>
#include <algorithm>
using namespace std;
int p[1000], b[1000];
int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int n, c, m;
    scanf("%d%d%d", &n, &c, &m);
    int x = 0, y = 0, z = 0;
    for (int i = 0; i < m; ++i) {
      scanf("%d%d", &p[i], &b[i]);
      if (p[i] == 1) ++x;
      if (b[i] == 1) ++y;
      if (b[i] == 2) ++z;
    }
    if (x > y && x > z) {
      printf("Case #%d: %d 0\n", ti + 1, x);
    } else {
      if (z > y) {
        for (int i = 0; i < m; ++i) b[i] = 3 - b[i];
      }
      int a[3][1001] = {};
      for (int i = 0; i < m; ++i) {
        ++a[b[i]][p[i]];
      }
      int ans = 0;
      for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
          int x = min(a[2][i], a[1][j]);
          a[2][i] -= x, a[1][j] -= x;
        }
        for (int j = 1; j < i; ++j) {
          int x = min(a[2][i], a[1][j]);
          a[2][i] -= x, a[1][j] -= x;
        }
        if (a[2][i]) {
          ans += a[2][i];
          a[1][i] -= a[2][i];
          a[2][i] = 0;
        }
      }
      printf("Case #%d: %d %d\n", ti + 1, max(y, z), ans);
    }
  }
  return 0;
}
