#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cout << "Case #" << cs << ": ";
    string s;
    int k;
    cin >> s >> k;
    int res = 0;
    for (int i = 0; i + k <= s.size(); ++i) {
      if (s[i] == '+') continue;
      for (int j = i; j < i + k; ++j) {
        s[j] = s[j] ^ '+' ^ '-';
      }
      ++res;
    }
    for (char c : s) {
      if (c == '-') {
        res = -1;
      }
    }
    if (res == -1) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << res << '\n';
    }
  }
}

