#include <iostream>
#include <string>
using namespace std;
int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    string s;
    int k;
    cin >> s >> k;
    int cnt = 0, flag = true;
    int n = s.length();
    for (int i = 0; i <= n - k; i++) {
      if (s[i] == '-') {
        cnt++;
        for (int j = 0; j < k; j++) {
          s[i + j] = s[i + j] == '+' ? '-' : '+';
        }
      }
    }
    for (int i = 0; i < n; i++) {
      if (s[i] == '-') {
        flag = false;
      }
    }
    cout << "Case #" << tk1 << ": ";
    if (flag) {
      cout << cnt << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
