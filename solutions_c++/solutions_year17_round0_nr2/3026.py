#include <bits/stdc++.h>

using namespace std;

int main() {
  int n; cin >> n;
  for (int t = 1; t <= n; t++) {
    string s; cin >> s;
    while (1) {
      bool c = true;
      for (int i = 1; i < s.size(); i++) {
        if (s[i-1] > s[i]) {
          s[i-1] = s[i-1]-1;
          for (int j = i; j < s.size(); j++) {
            s[j] = '9';
          }
          c = false;
          break;
        }
      }
      if (c) break;
    }
    int k = 0;
    while (s[k] == '0') k++;
    cout << "Case #" << t << ": " << s.substr(k) << endl;
  }
  return 0;
}
