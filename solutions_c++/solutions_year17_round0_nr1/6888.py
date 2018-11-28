#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("a.in", "rt", stdin);
  freopen("a.out", "wt", stdout);
  int t; cin >> t;
  for(int tst = 1; tst <= t; ++tst) {
    string s; int k;
    cin >> s >> k;
    int n = s.size();
    int ans = 0;
    for(int i = 0; i + k <= n; ++i) {
      if(s[i] == '-') {
        for(int j = 0; j < k; ++j) {
          s[i + j] = '+' + '-' - s[i + j];
        }
        ans++;
      }
    }
    cout << "Case #" << tst << ": ";
    if(count(s.begin(), s.end(), '+') == n) {
      cout << ans << endl;
    }else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
