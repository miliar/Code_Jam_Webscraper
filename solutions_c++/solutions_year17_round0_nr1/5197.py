#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    string s;
    int n;
    cin >> s >> n;
    string ideal(s.size(), '+');
    int res = 0;
    while (s != ideal && res >= 0) {
      for (int j = 0; j < s.size(); j++) {
        if (s[j] == '-') {
          res++;
          if (j + n <= s.size()) {
            for (int k = j; k < j + n; k++) {
              if (s[k] == '-') {
                s[k] = '+';
              } else {
                s[k] = '-';
              }
            }
          } else {
            res = -1;
          }
          break;
        }
      }
    }
    cout << "Case #" << i + 1 << ": " << (res == -1 ? "IMPOSSIBLE" : to_string(res)) << endl;   
  }

}