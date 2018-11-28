#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) (v).begin(), (v).end()
#define eb emplace_back
#define fi first
#define se second

using namespace std;

const int M = 1 << 20;

void solve() {
  string s;
  int k;
  cin >> s >> k;
  int n = s.length();
  int r = 0;
  for (int i = 0; i + k - 1 < n; ++i) {
    if (s[i] == '-') {
      for (int j = 0; j < k; ++j) {
        s[i+j] = s[i+j] == '+' ? '-' : '+';
      }
      r += 1;
    }
  }
  if (s == string(n, '+'))
    cout << r << '\n';
  else cout << "IMPOSSIBLE\n";
}

int main() {
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
