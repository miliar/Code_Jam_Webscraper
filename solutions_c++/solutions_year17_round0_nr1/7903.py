#include <iostream>
#include <string>
#include <queue>

using namespace std;

void solve(string s, int k) {
  int ans = 0;
  for (size_t i = 0; i < s.size(); ++i) {
    if (s[i] == '-') {
      if (i + k <= s.size()) {
        ans++;
        for (size_t j = i; j < i + k; ++j) {
          s[j] = (s[j] == '+') ? '-' : '+';
        }
      } else {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
    }
  }
  cout << ans << endl;
}

int main() {
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    string s;
    int k;
    cin >> s >> k;

    solve(s, k);



  }
  return 0;
}