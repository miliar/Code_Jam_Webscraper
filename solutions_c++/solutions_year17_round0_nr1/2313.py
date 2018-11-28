#include <bits/stdc++.h>

using namespace std;

int solve(string& s, int k) {
  int ans = 0;
  for (int i = 0; i + k - 1 < s.size(); i++) {
    if (s[i] == '-') {
      for (int j = i; j < i + k; j++) {
        if (s[j] == '-') {
          s[j] = '+';
        } else {
          s[j] = '-';
        }
      }
      ans++;
    }
  }

  for (auto c : s) {
    if (c == '-') {
      return -1;
    }
  }

  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    string s;
    int k;
    cin >> s >> k;
    int ans = solve(s, k);
    cout << "Case #" << tc << ": ";
    if (ans == -1) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << ans << '\n';
    }
  }
}
