#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) (v).begin(), (v).end()
#define eb emplace_back
#define fi first
#define se second

using namespace std;

typedef long long i64;

string solve() {
  string s;
  cin >> s;
  int n = s.length();
  if (n <= 1) return s;
  for (int i = 1; i < n; ++i) {
    if (s[i-1] > s[i]) {
      if (s[i-1] == '1') return string(n-1,'9');
      s[i-1] -= 1;
      i-=1;
      while (i>0&&s[i-1] > s[i]) {--i; s[i]-=1;}
      for (int j = i+1; j < n; ++j) s[j] = '9';
      return s;
    }
  }
  return s;
}

int main() {
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    cout << solve() << '\n';
  }
  return 0;
}
