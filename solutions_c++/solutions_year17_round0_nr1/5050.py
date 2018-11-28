#include <bits/stdc++.h>

using namespace std;

void solve() {
  string s;
  int k;
  cin >> s >> k;
  int ans = 0;
  for (int i = 0; i + k - 1 < s.size(); ++i) {
    if (s[i] == '-') {
      ans++;
      for (int j = i; j < i + k; ++j) {
        s[j] = (s[j] == '-' ? '+' : '-');
      }
    }
  }
  for (char c: s) {
    if (c == '-') {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << ans << endl;
  return;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}