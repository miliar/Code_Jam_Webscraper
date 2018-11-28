#include <iostream>
#include <string>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, i;
  cin >> t;
  string s;
  for (int _case = 1; _case <= t; _case++) {
    cin >> s;
    if (s.length() > 1) {
      for (i = 0; (i < s.length()-1) && (s[i] <= s[i+1]); ++i)
      {}

      if (i < s.length() - 1) {
        for (int j = i+2; j < s.length(); j++) {
          s[j] = '9';
        }
        for (;i >= 0 && s[i] > s[i+1]; i--) {
          s[i] = s[i]-1;
          s[i+1] = '9';
        }
        if (s[0] == '0') {
          s = s.substr(1, s.length()-1);
        }
      }
    }
    cout << "Case #" << _case << ": " << s << "\n";
  }
  return 0;
}
