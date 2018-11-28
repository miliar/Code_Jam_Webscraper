#include <bits/stdc++.h>
using namespace std;

void solve() {
  string s; int k;
  cin >> s >> k;
  int ans = 0;
  for (int i = 0; i + k <= s.size(); i++) {
    if (s[i] == '-') {
      for (int j = 0; j < k; j++) {
        s[i + j] = s[i + j] == '+' ? '-' : '+';
      }
      ans++;
    }
  }
  for (char ch: s) if (ch == '-') {
    cout << "IMPOSSIBLE";
    return;
  }
  cout << ans;
}

int main() {
  ios_base::sync_with_stdio(false);
  int tt; cin >> tt;
  for (int t = 1; t <= tt; t++) {
    cout << "Case #" << t << ": ";
    solve();
    cout << '\n';
  }
}
