#include <iostream>
#include <string>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, i, k;
  cin >> t;
  string s;
  int ans,p;
  for (int _case = 1; _case <= t; _case++) {
    ans = 0;
    cin >> s >> k;
    int p = 0;
    bool good = false;
    while (p < 10000 && !good) {
      p++;
      good = true;
      for (i = 0; i < s.length(); i++) {
        if (s[i] == '-') {
          good = false;
          ans++;
          for (int j = 0; (j < k) && (j+i < s.length()); ++j) {
            if (s[i+j] == '-') {
              s[i+j] = '+';
            } else {
              s[i+j] = '-';
            }
          }
          if (s.length() - i < k) {
            for (int j = 1; j <= k-(s.length() - i); j++) {
              if (s[i-j] == '-') {
                s[i-j] = '+';
              } else {
                s[i-j] = '-';
              }
            }
          }
        }
      }
    }
    if (good) {
      cout << "Case #" << _case << ": " << ans << "\n";
    } else {
      cout << "Case #" << _case << ": " << "IMPOSSIBLE" << "\n";
    }
  }
  return 0;
}
