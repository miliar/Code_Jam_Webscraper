#include <bits/stdc++.h>

using namespace std;

void solve() {
  string s;
  cin >> s;
  int l = s.length();
  int cur_i = 0;
  bool invert = false;
  for(int i = 1; i < l; i++) {
    if(invert) {
      s[i] = '9';
      continue;
    }
    if(s[cur_i] < s[i]) {
      cur_i = i;
    } else if (s[cur_i] > s[i]) {
      s[cur_i] = (char)s[cur_i] - 1;
      i = cur_i;
      invert = true;
    }
  }

  //Remove leading zeros
  int s_i;
  for(s_i = 0; s_i < l; s_i++) {
    if(s[s_i]!='0') break;
  }
  for(;s_i < l; s_i++) {
    cout << s[s_i];
  }
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
