#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 10;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    cout << "Case #" << qq << ": ";
    string s; int k;
    vector<int> si;
    cin >> s >> k;
    const int n = s.length();
    for (auto & e : s) si.push_back((e == '-'));
    int ans = 0, i = 0;
    for (; i + k <= n; i++) {
      if (si[i]) {
        ++ans;
        for (int d = 0; d < k; d++) si[i + d] = !si[i + d];
      }
    }
    for (; i < n; i++) if (si[i]) ans = -1;
    if (ans == -1) cout << "IMPOSSIBLE\n";
    else cout << ans << "\n";
  }
  return 0;
}
