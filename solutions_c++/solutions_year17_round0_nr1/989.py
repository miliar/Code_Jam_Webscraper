#include <iostream>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    string s; cin >> s;
    int k; cin >> k;
    int res = 0;
    for (int i = 0; i+k <= s.size(); i++) {
      if (s[i] == '-') {
        res++;
        for (int j = 0; j < k; j++) {
          if (s[i+j] == '-') s[i+j] = '+';
          else s[i+j] = '-';
        }
      }
    }

    bool success = true;
    for (int i = 0; i < s.size(); i++)
      success = success && s[i] == '+';
    cout << "Case #" << c << ": " << (success ? to_string(res) : "IMPOSSIBLE") << endl;
  }
  return 0;
}
