#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;

int main() {
  ios_base::sync_with_stdio(false);
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    string s; cin >> s;
    int k, n = s.size(), res = 0; cin >> k;
    vector<char> a(n);
    for (int j = 0; j < n; ++j) a[j] = s[j];

    for (int j = 0; j < n; ++j) {
      if (a[j] == '-' && j + k <= n) {
        for (int l = j; l < j + k; ++l) {
          if (a[l] == '-') a[l] = '+';
          else a[l] = '-';
        }
        res++;
      }
    }
    for (int j = 0; j < n; ++j) {
      if (a[j] == '-') res = -1;
    }

    cout << "Case #" << i << ": ";
    if (res >= 0) cout << res;
    else cout << "IMPOSSIBLE";
    cout << endl;
  }

  return 0;
}
