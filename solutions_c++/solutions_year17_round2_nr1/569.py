#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    double d;
    int n;
    cin >> d >> n;
    double time = 0.0;
    for (int i = 0; i < n; i++) {
      double k, s;
      cin >> k >> s;
      time = max(time, (d - k) / s);
    }
    double ans = d / time;

    cout << "Case #" << tc << ": " << fixed << setprecision(9) << ans << '\n';
  }

}
