#include <bits/stdc++.h>
using namespace std;

char swap(char c) {
  if(c == '-') {
    return '+';
  } else {
    return '-';
  }
}

int main() {
  bool same;
  int tt, l, ans;
  string s;
  cin >> tt;
  for(int i = 0; i < tt; i++) {
    same = true;
    ans = 0;
    cin >> s >> l;
    for(int j = 0; j <= s.length() - l; j++) {
      if(j == s.length() - l) {
        char c = s[j];
        for(int k = j + 1; k < s.length(); k++) {
          if(s[k] != c) {
            same = false;
            break;
          }
        }
        if(same && c == '-') {
          ans++;
        }
      } else if(s[j] == '-') {
        ans++;
        for(int k = 1; k < l; k++) {
          s[j+k] = swap(s[j+k]);
        }
      }
    }
    if(same) {
      cout << "Case #" << i+1 << ": " << ans << endl;
    } else {
      cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    }
  }

  return 0;
}