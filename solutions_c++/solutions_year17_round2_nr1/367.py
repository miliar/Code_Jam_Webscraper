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

int main(void) {
  size_t T;
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    size_t n,d;
    cin >> d >> n;
    double t = 0;
    for (size_t i = 0; i < n; i++) {
      double k,s;
      cin >> k >> s;
      t = max(t,(d-k)/s);
    }
    cout << "Case #" << tt+1 << ": ";
    cout << fixed << setprecision(10) << d/t << endl;
  }
  return 0;
}
