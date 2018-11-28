#include <string>
#include <iostream>

using namespace std;

void change(char &a) {
  if (a == '+') a = '-';
  else a = '+';
}

int main() {
  ios::sync_with_stdio(false);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    int c = 0;
    for (int i = 0; i + k <= n; ++i) {
      if (s[i] == '-') {
        ++c;
        for (int j = 0; j < k; ++j) change(s[i + j]);
      }
    }
    for (int i = n - k + 1; i < n; ++i) {
      if (s[i] == '-') c = -1;
    }
    cout << "Case #" << t << ": ";
    if (c == -1) cout << "IMPOSSIBLE" << endl;
    else cout << c << endl;
  }
}
