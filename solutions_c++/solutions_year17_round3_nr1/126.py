#include <cstdio>
#include <utility>
#include <functional>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<ll, int> pli;
const int N = 1000;
const double PI = atan(1) * 4;
int r[N], h[N];
pli a[N];

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
      scanf("%d%d", &r[i], &h[i]);
    }
    double ans = 0;
    for (int i = 0; i < n; ++i) {
      int c = 0;
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        a[c++] = pli((ll)r[j] * h[j], j);
      }
      sort(a, a + n - 1, greater<pli>());
      int rm = r[i];
      ll rhs = (ll)r[i] * h[i];
      for (int j = 0; j < k - 1; ++j) {
        rm = max(rm, r[a[j].second]);
        rhs += a[j].first;
      }
      ans = max(ans, (rhs * 2 + (ll)rm * rm) * PI);
    }
    printf("Case #%d: %.9f\n", ti + 1, ans);
  }
  return 0;
}
