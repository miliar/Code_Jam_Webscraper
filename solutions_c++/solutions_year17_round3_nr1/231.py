#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

const double PI = acos(-1.0);

struct Cake {
  double r, h;
} c[1010];

Cake b[1010];

bool CmpR(const Cake &c1, const Cake &c2) {
  if (c1.r != c2.r) return c1.r < c2.r;
  return c1.h < c2.h;
}

bool CmpA(const Cake &c1, const Cake &c2) {
  return c1.r * c1.h > c2.r * c2.h;
}

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/A-large.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/A-large.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
      scanf("%lf%lf", &c[i].r, &c[i].h);
    }
    sort(c, c + n, CmpR);
    memcpy(b, c, sizeof(Cake) * n);
    double ans = 0;
    for (int i = k - 1; i < n; ++i) {
      double tmp = c[i].r * c[i].r + 2 * c[i].h * c[i].r;
//      printf("i =%d tm=%f\n",i,tmp);
      sort(b, b + i, CmpA);
      for (int j = 0; j< i; ++j) {
//        printf("b%d r=%d h=%d\n",j, b[j].r, b[j].h);
      }
      for (int j = 0; j < k - 1; ++j) {
        tmp += 2 * b[j].h * b[j].r;
      }
      ans = max(ans, tmp);
//      printf("tmp %f ans=%f\n", tmp, ans);
    }
    printf("Case #%d: %.9f\n", ++tc, ans * PI);
  }
  return 0;
}