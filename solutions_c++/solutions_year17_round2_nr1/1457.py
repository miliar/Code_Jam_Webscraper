#include <bits/stdc++.h>

using namespace std;

void solve() {
  double d;
  double n;
  cin >> d >> n;
  double max_h = 0;
  double k;
  double s;
  for(int i = 0; i < n; i++) {
    cin >> k >> s;
    max_h = max(max_h, (d-k)/s);
  }
  cout << fixed << setprecision(6) << d / max_h;
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
