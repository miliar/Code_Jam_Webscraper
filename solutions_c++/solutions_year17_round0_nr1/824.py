#include <bits/stdc++.h>

using namespace std;

int main() {
  int test;
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    string s;
    int k;
    cin >> s >> k;
    int len = s.length(), ans = 0;
    for (int i = 0; i + k <= len; ++i) {
      if (s[i] == '-') {
        ++ans;
        for (int j = i; j < i + k; ++j) {
          s[j] = '-' + '+' - s[j];
        }
      }
    }
    bool flag = 1;
    for (int i = 0; i < len; ++i) {
      flag &= s[i] == '+';
    }
    cout << "Case #" << ca << ": ";
    if (flag) {
      cout << ans << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
