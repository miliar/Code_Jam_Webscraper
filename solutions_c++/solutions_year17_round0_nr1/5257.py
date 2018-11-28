#include <bits/stdc++.h>
using namespace std;

int i, j, test, tests, rs, k, n;
string s;

int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> s >> k; n = s.size();

    for(rs = i = 0; i + k - 1 < n; ++i) {
      if(s[i] == '+') continue;

      for(++rs, j = 0; j < k; ++j) s[i + j] = (s[i + j] == '-' ? '+' : '-');
    }

    bool ok = 1;
    for(auto it : s) if(it == '-') ok = 0;

    if(ok) cout << rs << '\n';
    else cout << "IMPOSSIBLE\n";
  }

  return 0;
}