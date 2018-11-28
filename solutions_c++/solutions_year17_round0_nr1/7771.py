#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main() {
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    string s;
    int k;
    cin >> s >> k;
    bool ok = true;
    int n = 0;
    for (int i = 0; i < s.length(); ++i) {
      if (s[i] == '-') {
        if (i + k > s.length()) {
          ok = false;
        } else {
          for (int j = 0; j < k; ++j) {
            s[i+j] = s[i+j] == '+' ? '-' : '+';
          }
          n++;
        }
      }
    }
    cout << "Case #" << t + 1 << ": ";
    if (ok) cout << n;
    else cout << "IMPOSSIBLE";
    cout << endl;
  }
}
