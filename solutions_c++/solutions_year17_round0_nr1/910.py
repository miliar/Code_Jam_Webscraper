#include <bits/stdc++.h>
using namespace std;

bool exist_blank(const string &s, int k) {
  int last_index = s.size() - 1;
  for (int i = 0; i < k; i++) {
    if (s[last_index - i] == '-') {
      return false;
    }
  }
  return true;
}

int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    string s;
    int k;
    int count = 0;
    cin >> s >> k;
    int len = s.size();
    for (int i = 0; i + k - 1 < len; i++) {
      if (s[i] == '-') {
        count++;
        for (int j = 0; j < k; j++) {
          s[i+j] = (s[i+j] == '-') ? '+' : '-';
        }
      }
    }
    cout << "Case #" << tc << ": ";
    if (exist_blank(s, k)) {
      cout << count << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
