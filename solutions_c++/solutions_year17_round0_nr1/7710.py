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
    string s;
    cin >> s;
    int n = s.length(), k;
    cin >> k;

    cout << "Case #" << cs + 1 << ": ";

    for (int i = 0, ans = 0; i <= n; i++) {
      if (i == n) {
        cout << ans << endl;
      } else if (s[i] == '-') {
        if (i <= n - k) {
          for (int j = 0; j < k; j++)
            s[i + j] = s[i + j] == '+' ? '-' : '+';
          ans++;
        } else {
          cout << "IMPOSSIBLE" << endl;
          break;
        }
      }
    }
  }

  return 0;
}
