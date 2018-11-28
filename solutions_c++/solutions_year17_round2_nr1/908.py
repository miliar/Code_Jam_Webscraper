#include <algorithm>
#include <cstdio>
#include <cmath>

typedef long double Double;

const int N = 1000 + 10;
const Double INF = 1E30;

struct Horse {
  Double s, k;

  bool operator < (const Horse& other) const {
    return k < other.k;
  }
} horses[N];

int n, d;

bool Check(Double v) {
  for (int i = n; i >= 1; -- i) {
    if (v > horses[i].s && horses[i].k * v < d * (v - horses[i].s)) {
      return false;
    }
  }
  return true;
}

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    scanf("%d%d", &d, &n);
    double answer = 1e30;
    for (int i = 1; i <= n; ++ i) {
      scanf("%Lf%Lf", &horses[i].k, &horses[i].s);
      double x = (d * horses[i].s) / (d - horses[i].k);
      answer = std::min(answer, x);
      // if (t == 37) {
      //   printf("%d %Lf %Lf\n", d, horses[i].k, horses[i].s);
      // }
    }
    // std::sort(horses + 1, horses + n + 1);

    // Double l = 0, r = 1e20;
    // for (int times = 0; times < 200; ++ times) {
    //   Double m = (l + r) / 2;
    //   if (Check(m)) {
    //     l = m;
    //   } else {
    //     r = m;
    //   }
    // }
    printf("Case #%d: %.7lf\n", t, answer);
  }
  return 0;
}