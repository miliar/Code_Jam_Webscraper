#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

void solve() {
  int d, n;
  cin >> d >> n;
  vector<pair<int, int>> h(n);
  for (int i = 0; i < n; i++) {
    cin >> h[i].first >> h[i].second;
  }
  sort(h.begin(), h.end());
  double l = 0, r = 1e14;
  for (int i = 0; i < 100; i++) {
    double m = (l + r) / 2;
    bool yes = true;
    for (int i = 0; i < n; i++) {
      if (m > h[i].second && h[i].first / (m - h[i].second) * m < d) {
        yes = false;
      }
    }
    if (yes) {
      l = m;
    } else {
      r = m;
    }
  }
  printf(" %.10f\n", l);
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ":";
    solve();
  }
}
