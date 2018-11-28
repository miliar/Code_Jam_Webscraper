#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int n, k;
string s;
int main() {
  cin >> n;

  for (int tc = 1; tc <= n; tc++) {
    int ans = 0;
    bool can = true;
    cin >> s >> k;
    int len = (int)s.length();
    for (int i = 0; i + k - 1 < len; i++) {
      if (s[i] == '-') {
        for (int j = i; j <= i + k - 1; j++) {
          if (s[j] == '-') s[j] = '+';
          else if (s[j] == '+') s[j] = '-';
        }
        ans++;
      }
    }
    for (int i = 0; i < len; i++) {
      if (s[i] == '-') can = false;
    }
    printf("Case #%d: ", tc);
    if (!can) puts("IMPOSSIBLE");
    else cout << ans << endl;
  }
  return 0;
}
