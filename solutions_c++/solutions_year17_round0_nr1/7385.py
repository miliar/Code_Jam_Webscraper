#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;

void solve() {
  
  int k, ans = 0;
  string s;

  cin >> s >> k;

  for (int i = 0; i+k <= s.length(); i++) {
    if (s[i] == '+') {
      continue;
    }
    for (int j = 0; j < k; j++) {
      s[i+j] = s[i+j] == '-' ? '+' : '-';
    }
    ans++;
  }
  for (char c : s) {
    if (c == '-') {
      ans = INT_MAX;
    }
  }
  if (ans == INT_MAX) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << ans << endl;
  }
}

int main() { _
  int T;
  cin >> T;

  for (int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";
    solve();
  }
  return 0;
}

