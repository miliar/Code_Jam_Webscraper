#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string s;
    cin >> s;
    int K;
    cin >> K;

    int ans = 0;

    for (size_t i = 0; i <= s.size() - K; i++) {
      if (s[i] == '-') {
        ans ++;
        for (size_t j = i; j < i + K; j++) {
          if (s[j] == '-') s[j] = '+';
          else if (s[j] == '+') s[j] = '-';
        }
      }
    }

    for (size_t i = s.size() - K + 1; i < s.size(); i++) {
      if (s[i] == '-') {
        ans = -1;
        break;
      }
    }

    if (ans >= 0) cout << "Case #" << t << ": " << ans << endl;
    else cout << "Case #" << t << ": IMPOSSIBLE" << endl;
  }
}
