/*
ID: ebappa11
PROG: wormhole
LANG: C++11
*/

#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);

  int t;
  cin >> t;

  for (int cs = 0; cs < t; cs++) {
    double d;
    int n;
    cin >> d >> n;

    double ans = 1e18;
    for (int i = 0; i < n; i++) {
      double k, s;
      cin >> k >> s;
      ans = min(ans, s * d / (d - k));
    }

    cout << "Case #" << cs + 1 << ": ";
    cout << fixed << setprecision(6) << ans << endl;
  }

  return 0;
}
