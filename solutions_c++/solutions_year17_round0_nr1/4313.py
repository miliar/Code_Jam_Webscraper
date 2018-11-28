// A.cpp
// Oversized Pancake Flipper

#include <iostream>
#include <string>
using namespace std;

int main() {
  int t, kase = 0;
  cin >> t;
  while (t--) {
    string s;
    int k, cnt = 0;
    cin >> s >> k;
    for (int i = 0; i < (int)s.size() - k + 1; i++) {
      if (s[i] != '+') {
        cnt++;
        for (int j = i; j < i + k; j++) {
          if (s[j] == '+') {
            s[j] = '-';
          } else {
            s[j] = '+';
          }
        }
      }
    }
    bool valid = true;
    for (int i = 0; i < (int)s.size(); i++) {
      if (s[i] == '-') {
        valid = false;
        break;
      }
    }
    cout << "Case #" << ++kase << ": ";
    if (valid) {
      cout << cnt << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
