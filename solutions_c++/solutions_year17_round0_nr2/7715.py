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
    int n = s.length();
    deque <int> d(n);
    for (int i = n - 1; i >= 0; i--) {
      d[i] = s[i] - '0';
      if (i != n - 1) {
        if (d[i] > d[i + 1]) {
          d[i]--;
          for (int j = i + 1; j < n; j++) {
            d[j] = 9;
          }
        }
      }
    }
    while (d.front() == 0) d.pop_front();
    cout << "Case #" << cs + 1 << ": ";
    for (int x: d) cout << x;
    cout << endl;
  }

  return 0;
}
