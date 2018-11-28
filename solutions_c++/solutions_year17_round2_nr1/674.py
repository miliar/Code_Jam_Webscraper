#include <bits/stdc++.h>

using namespace std;

const double INF = 1e20, eps = 1e-16;
const int N = 1010;

int n, d;
int k[N], s[N];

/*
bool check(long double mid) {
  long double x = 1.0 * d / mid;
  for (int i = 1; i <= n; ++i) {
    long double t = 1.0 * (d - s[i]) / k[i];
    if (t > x + eps) return 0;
  }
  return 1;
}*/

int main() {
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d%d", &d, &n);
    for (int i = 1; i <= n; ++i) {
      scanf("%d%d", k + i, s + i);
    }
    double mx = 0;
    for (int i = 1; i <= n; ++i) {
      double t = 1.0 * (d - k[i]) / s[i];
      mx = max(mx, t);
    }
    /*
    long double l = 0, r = INF;
    for (int i = 0; i < 100; ++i) {
      long double mid = (l + r) / 2;
      if (check(mid)) {
        l = mid;
      } else {
        r = mid;
      }
    }*/
    printf("Case #%d: %.8f\n", _, (double)d / mx);
  }
  return 0;
}
