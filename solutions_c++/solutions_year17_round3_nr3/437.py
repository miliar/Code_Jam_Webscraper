#include <iostream>
#include <algorithm>
using namespace std;
int main() {
  int t, tt, n, k, i, ok;
  double u, p[50], sum, avg, ans;
  cin >> t;
  for (tt = 1; tt <= t; tt++) {
    cin >> n >> k;
    cin >> u;
    sum = 0.0;
    for (i = 0; i < n; i++) {
      cin >> p[i];
      sum += p[i];
    }
    sort(p, p + n);
    ok = 0;
    ans = 1.0;
    for (i = n - 1; i >= 0; i--) {
      if (ok) {
        ans *= avg;
      } else {
        avg = (sum + u) / (i + 1);
        if (avg - p[i] > 1e-12) {
          ok = 1;
          ans *= avg;
        }
        else {
          sum -= p[i];
          ans *= p[i];
        }
      }
    }
    printf("Case #%d: %.6f\n", tt, ans);
  }
  return 0;
}
