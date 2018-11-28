#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; ++t) {
    int k;
    string s;
    cin >> s >> k;

    int ans = 0;
    for (int i = 0; i < s.size() - k + 1; ++i) {
      if (s[i] == '-') {
        ans++;
        for (int j = 0; j < k; ++j) {
          if (s[i + j] == '-') {
            s[i + j] = '+';
          } else {
            s[i + j] = '-';
          }
        }
      }
    }

    cout << "Case #" << t + 1 << ": ";
    if (count(begin(s), end(s), '-') == 0) {
      cout << ans << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
