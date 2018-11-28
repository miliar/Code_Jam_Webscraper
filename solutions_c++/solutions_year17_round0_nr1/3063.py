#include <bits/stdc++.h>

using namespace std;

char flip(char c) {
  if (c == '+') return '-';
  else return '+';
}

int main() {
  int n; cin >> n;
  for (int t = 1; t <= n; t++) {
    string s; cin >> s;
    int k; cin >> k;

    int ret = 0;
    bool found = false;
    while (1) {
      bool all = true;
      for (int i = 0; i < s.size(); i++) {
        all &= s[i] == '+';
      }
      if (all) break;
      bool z = false;
      for (int i = 0; i < s.size(); i++) {
        if (s[i] == '-') {
          if (i + k <= s.size()) {
            for (int j = i; j < i + k; j++) s[j] = flip(s[j]);
            ret++;
            bool zz = true;
            for (int j = i; j < i + k; j++) zz &= s[j] == '+';
            if (zz) z = true;
          }
        }
      }
      if (!z) {
        ret = -1;
        break;
      }
    }


    cout << "Case #" << t << ": ";
    if (ret == -1) cout << "Impossible" << endl;
    else cout << ret << endl;
  }

  return 0;
}
