#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
typedef pair<int, int> pii;
const double pi = acos(-1);
int cmp(pii a, pii b) {
  return 2 * pi * a.first * a.second > 2 * pi * b.first * b.second;
}
int main() {
  int t, tt, n, k, i, j;
  pii p[1000];
  double area, amax;
  cin >> t;
  for (tt = 1; tt <= t; tt++) {
    cin >> n >> k;
    for (i = 0; i < n; i++) {
      cin >> p[i].first >> p[i].second;
    }
    amax = 0;
    for (i = n - 1; i >= 0; i--) {
      sort(p, p + n);
      sort(p, p + i, cmp);
      area = pi * p[i].first * p[i].first + 2 * pi * p[i].first * p[i].second;
      for (j = 0; j < min(i, k - 1); j++) {
        area += 2 * pi * p[j].first * p[j].second;
      }
      amax = max(amax, area);
    }
    printf("Case #%d: %.9f\n", tt, amax);
  }
  return 0;
}
