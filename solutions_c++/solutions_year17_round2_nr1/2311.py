#include <bits/stdc++.h>
using namespace std;

int d, n;
double arrt[1010];

int main() {
  int kase;
  scanf("%d", &kase);
  for(int ka = 0; ka < kase; ka++) {
    scanf("%d%d", &d, &n);
    for(int i = 0; i < n; i++) {
      int x, y;
      scanf("%d%d", &x, &y);
      arrt[i] = (double) (d - x) / y;
    }
    double ma = 0;
    for(int i = 0; i < n; i++) {
      ma = max(ma, arrt[i]);
    }
    printf("Case #%d: %.6lf\n", ka + 1, d / ma);
  }
  return 0;
}
