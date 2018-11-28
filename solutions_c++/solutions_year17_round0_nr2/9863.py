#include <bits/stdc++.h>
using namespace std;

int find_bad(string s) {
  for (int i = 0; i < s.size()-1; ++i) {
    if (s[i] > s[i+1]) {
      return i;
    }
  }
  return -1;
}

string answer(string s) {
  int bad = find_bad(s);
  while (bad != -1) {
    if (bad == 0 && s[bad] == '1') {
      return string(s.size()-1, '9');
    }
    else {
      s[bad] = s[bad] - 1;
      for (int i = bad+1; i < s.size(); ++i) {
        s[i] = '9';
      }
    }
    bad = find_bad(s);
  }
  return s;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string s;
    cin >> s;
    cout << "Case #" << t << ": " << answer(s) << "\n";
  }
  return 0;
}
