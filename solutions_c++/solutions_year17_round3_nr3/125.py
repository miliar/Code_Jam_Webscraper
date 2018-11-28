#include <cstdio>
#include <algorithm>
using namespace std;
double u, p[51];
int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int n, k;
    scanf("%d%d%lf", &n, &k, &u);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &p[i]);
    }
    sort(p, p + n);
    p[n] = 2;
    double ans = 1;
    for (int i = 0; i < n; ++i) {
      double d = p[i + 1] - p[i];
      if (d * (i + 1) <= u) {
        u -= d * (i + 1);
      } else {
        double x = p[i] + u / (i + 1);
        for (int j = 0; j <= i; ++j) {
          ans *= x;
        }
        for (int j = i + 1; j < n; ++j) {
          ans *= p[j];
        }
        break;
      }
    }
    printf("Case #%d: %.9f\n", ti + 1, ans);
  }
  return 0;
}
