#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    string s;
    int k;
    cin >> s >> k;

    int n = s.size();
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (i + k > n) break;
      if (s[i] == '+') continue;

      ans++;
      for (int j = 0; j < k; ++j) {
        if (s[i + j] == '-') {
          s[i + j] = '+';
        } else {
          s[i + j] = '-';
        }
      }
    }

    int cnt = count(s.begin(), s.end(), '-');
    if (cnt) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << ans << endl;
    }
  }

  return 0;
}
