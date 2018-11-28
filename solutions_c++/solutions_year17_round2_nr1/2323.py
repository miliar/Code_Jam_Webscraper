#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; ++tt) {

    int d, n; cin >> d >> n;
    double mx = 0.0;
    for (int i = 0; i < n; ++i) {
      int k, s; cin >> k >> s;
      double tmp = (d - k) * 1.0 / s;
      mx = max(mx, tmp);
    }
    double speed = d * 1.0 / mx;
    printf("Case #%d: %.6f\n", tt, speed);

  }

  return 0;
}
