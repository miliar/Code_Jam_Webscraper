#include <bits/stdc++.h>
using namespace std;

int T, k;
string s;

int main() {

  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> s >> k;
    int ans = 0;
    for (int i = 0; i + k - 1 < s.length(); i++) {
      if (s[i] == '-') {
        ans++;
        for (int j = 0; j < k; j++) {
          if (s[i+j] == '-') {
            s[i+j] = '+';
          } else {
            s[i+j] = '-';
          }
        }
      }
    }
//cout << s << endl;
    for (int i = s.length() - k + 1; i < s.length(); i++) {
      if (s[i] == '-') {
        ans = -1;
      }
    }

    cout << "Case #" << t << ": ";
    if (ans != -1) {
      cout << ans << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}