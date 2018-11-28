#include <cmath>
#include <cstdio>
#include <algorithm>

const int N = 1000 + 10;
const double PI = acos(-1.);

int n, k, r[N], h[N];

double solve(int x) {
  static double a[N];
  int tot = 0;
  for (int i = 1; i <= n; ++i) if (i != x && r[i] <= r[x]) a[++tot] = 2. * PI * r[i] * h[i];
  double res = 2. * PI * r[x] * h[x] + PI * r[x] * r[x];
  std::sort(a + 1, a + tot + 1);
  std::reverse(a + 1, a + tot + 1);
  for (int i = 1; i < k && i <= tot; ++i) res += a[i];
  return res;
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; ++i) scanf("%d%d", &r[i], &h[i]);
    double ans = 0.;
    for (int i = 1; i <= n; ++i) ans = std::max(ans, solve(i));
    printf("Case #%d: %.12f\n", tid, ans);
  }
  return 0;
}
