// TEMPLATE {{{
#include <bits/stdc++.h>
using namespace std;
#ifndef LOCAL
#define OJ 1
#else
#define OJ 0
#endif

#define endl '\n'
#define TIMESTAMP merr << "Execution time: " << (double)clock()/CLOCKS_PER_SEC << " s.\n"
class C_ {}; template <typename T> C_& operator <<(C_& __m, const T& __s) { if (!OJ) cerr << "\E[91m" << __s << "\E[0m"; return __m; }
C_ merr;

struct __s { __s() { if (OJ) { ios_base::Init i; cin.sync_with_stdio(0); cin.tie(0); } } ~__s(){ TIMESTAMP; } } __S;
/// END OF TEMPLATE }}}

#define size_t unsigned long long

bool ok(const string & s) {
  for (char c : s) {
    if (c != '+') return false;
  }
  return true;
}

string flip(const string & s, size_t from, size_t k) {
  string res = s;
  for (size_t i = 0; i < k; i++) {
    if (i+from >= s.size()) return s;
    res[i+from] = (res[i+from] == '+' ? '-' : '+');
  }
  return res;
}

string solve(string s, size_t k) {
  size_t res = 0;
  for (size_t i = 0; i < s.size(); i++) {
    if (s[i] == '-') {
      s = flip(s, i, k);
      res++;
    }
  }
  if (ok(s)) return to_string(res);
  return "IMPOSSIBLE";
}

int main(void) {
  size_t T;
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    string s;
    size_t k;
    cin >> s >> k;
    string ans = solve(s, k);
    reverse(s.begin(), s.end());
    assert(ans == solve(s,k));
    cout << "Case #" << tt+1 << ": ";
    cout << ans << endl;
  }
  return 0;
}
