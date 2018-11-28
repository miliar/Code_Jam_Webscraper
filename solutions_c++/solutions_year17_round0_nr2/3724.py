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

bool tidy(size_t x) {
  size_t prev = 10;
  while (x) {
    size_t d = x%10;
    x /= 10;
    if (d > prev) return false;
    prev = d;
  }
  return true;
}

size_t brute(size_t x) {
  for (size_t i = x; i >= 1; i--) {
    if (tidy(i)) return i;
  }
  return 1;
}

string clever(size_t x) {
  string s = to_string(x);
  size_t len = s.size();
  for (size_t i = 0; i+1 < len; i++) {
    if (s[i] > s[i+1]) {
      if (s[i] == '1') {
        string res;
        for (size_t j = 0; j < len-1; j++) {
          res += '9';
        }
        return res;
      } else {
        size_t idx = i;
        while (idx > 0 && s[idx-1]==s[i]) idx--;
        s[idx]--;
        for (size_t j = idx+1; j < len; j++) {
          s[j] = '9';
        }
        return s;
      }
    }
  }
  return s;
}

int main(void) {
  // for (size_t i = 1; i < 10000000; i++) {
    // merr << '\r' << i << '\r';
    // assert(to_string(brute(i)) == clever(i));
  // }
  // return 0;
  size_t T;
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    size_t x;
    cin >> x;
    cout << "Case #" << tt+1 << ": ";
    // cout << brute(x) << endl;
    cout << clever(x) << endl;
  }
  return 0;
}
