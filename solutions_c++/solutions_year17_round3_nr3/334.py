#include <cstdio>
#include <algorithm>

const int N = 50 + 10;

int n, m;
double p[N], tot;

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d%lf", &n, &m, &tot);
    for (int i = 1; i <= n; ++i) scanf("%lf", &p[i]);
    std::sort(p + 1, p + n + 1);
    p[n + 1] = 1.;
    for (int i = 1; i <= n; ++i) {
      double cur = std::min(tot / i, p[i + 1] - p[i]);
      for (int j = 1; j <= i; ++j) p[j] += cur;
      tot -= i * cur;
    }
    double ans = 1.;
    for (int i = 1; i <= n; ++i) ans *= p[i];
    printf("Case #%d: %.12f\n", tid, ans);
  }
  return 0;
}
