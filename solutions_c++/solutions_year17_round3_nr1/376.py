#include <bits/stdc++.h>
using namespace std;

const double pi = acos(-1);

struct cake {
  double r;
  double h;
  bool operator< (const cake& c2) const {
    return r > c2.r;
  }
} cakes[1010];

int n, k;

int main() {
  int kase;
  scanf("%d", &kase);
  for(int ka = 0; ka < kase; ka++) {
    scanf("%d%d", &n, &k);
    for(int i = 0; i < n; i++) {
      scanf("%lf%lf", &cakes[i].r, &cakes[i].h);
    }
    double ma = 0;
    sort(cakes, cakes + n);
    for(int i = 0; i < n - k + 1; i++) {
      vector<double> areas;
      for(int j = i + 1; j < n; j++) {
        areas.push_back(2 * pi * cakes[j].r * cakes[j].h);
      }
      sort(areas.begin(), areas.end());
      reverse(areas.begin(), areas.end());
      double out = pi * cakes[i].r * cakes[i].r + 2 * pi * cakes[i].r * cakes[i].h;
      for(int j = 0; j < k - 1; j++) {
        out += areas[j];
      }
      ma = max(ma, out);
    }
    printf("Case #%d: %.9lf\n", ka + 1, ma);
  }
  return 0;
}
