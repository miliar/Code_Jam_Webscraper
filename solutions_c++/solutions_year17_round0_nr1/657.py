#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int tc = 1; tc <= T; tc++) {
    string s;
    int k;
    cin >> s >> k;

    int ans = 0;

    for (int i = 0; i + k <= s.size(); i++) {
      if (s[i] == '-') {
        ++ans;
        for (int j = i; j < i + k; j++) {
          s[j] = (s[j] == '-') ? '+' : '-';
        }
      }
    }

    cout << "Case #" << tc << ": ";

    if (count(s.begin(), s.end(), '+') != s.size()) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << ans << "\n";
    }
  }

  return 0;
}
