#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
  double d;
  int n;
  cin >> d >> n;
  vector <double> pos(n), speed(n);
  for (int i = 0; i < n; ++i) {
    cin >> pos[i] >> speed[i];
  }
  double l = 0, r = 1e18;
  for (int step = 0; step < 100; ++step) {
    double v = (l + r) / 2;
    double time_needed = d / v;
    bool good = 1;
    for (int i = 0; i < n; ++i) {
      if ((v - speed[i]) * time_needed <= pos[i]) {
        continue;
      } else {
        good = 0;
        break;
      }
    }
    if (good) {
      l = v;
    } else {
      r = v;
    }
  }
  cout << l << endl;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  cout.precision(10);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}