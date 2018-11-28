#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve() {
  string s;
  cin >> s;
  int k;
  cin >> k;

  const int n = s.size();
  vector<bool> arr(n, false);
  bool cur = false;
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    cur ^= arr[i];
    if (cur) {
      if (s[i] == '-') s[i] = '+';
      else s[i] = '-';
    }
    
    if (s[i] == '-') {
      s[i] = '+';
      cur ^= true;
      if (i + k > n) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
      if (i + k < n)
        arr[i + k] = true;
      ans++;
    }
  }

  cout << ans << endl;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    solve();
  }
}
