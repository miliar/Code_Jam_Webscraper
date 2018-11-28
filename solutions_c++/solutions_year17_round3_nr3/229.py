#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

const double EPS = 1e-9;

int Cmp(double a, double b) {
  if (fabs(a - b) < EPS) return 0;
  if (a > b) return 1;
  return -1;
}

double p[50];

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/C-small-1-attempt0.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/C-small.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    double ans;
    int n, k;
    double r;
    scanf("%d%d", &n, &k);
    scanf("%lf", &r);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &p[i]);
    }
    sort(p, p + n);
//    for (int i = 0; i < n; ++i) { printf("p %d %f\n", i, p[i]);}
    while (r > EPS) {
      int i;
      for (i = 1; i < n; ++i) {
        if (Cmp(p[i], p[i - 1])) {
          break;
        }
      }
      double t;
//      printf("i= %d r= %f\n", i, r);
      if (i == n) {
        t = r / n;
      } else {
        t = min(p[i] - p[i - 1], r / i);
      }
      r -= i * t;
      for (int j = 0; j < i; ++j) {
        p[j] += t;
//        printf("p[%d]+ %f=> %f\n", j, t, p[j]);
      }
    }

    ans = 1.0;
    for (int i = 0; i < n; ++i) {
      ans *= min(1.0, p[i]);
    }
    printf("Case #%d: %.6f\n", ++tc, ans);
  }
  return 0;
}