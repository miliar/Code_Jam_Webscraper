#include <iostream>
#include <string>
using namespace std;

void solve() {
  string s;
  cin >> s;
  int k;
  cin >> k;
  int ans = 0;
  for (size_t i = 0; i + k <= s.size(); ++i) {
    if (s[i] == '-') {
      ans++;
      for (int j = 0; j < k; ++j) {
        if (s[j + i] == '-')
          s[j + i] = '+';
        else
          s[j + i] = '-';
      }
    }
  }
  bool fail = false;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == '-') fail = true;
  }
  if (fail)
    cout << "IMPOSSIBLE";
  else
    cout << ans;
}
int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
}
