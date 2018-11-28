#include <string>
#include <functional>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main () {
freopen("data.txt", "r", stdin);
freopen("result.txt", "w", stdout);

int T;
cin >> T;

for (int _t = 1; _t <= T; _t++) {


  string s;
  int k;
  cin >> s >> k;

  int ans = 0;

  for (int i = 0; i <= s.length() - k; ++i) {
    if (s[i] == '+') continue;

    for (int j = i; j < i + k; ++j) {
      s[j] = s[j] == '+' ? '-' : '+';
    }
    ans++;
  }

  cout << "Case #" << _t << ": ";
  if (count(s.end() - k, s.end(), '+') == k)  cout << ans; else cout << "IMPOSSIBLE";
  cout << endl;
}

return 0;
}
