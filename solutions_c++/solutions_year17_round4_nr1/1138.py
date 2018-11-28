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

size_t solve2(const vector<size_t> & A) {
  size_t P[2] = {};
  for (auto x : A) { P[x%2]++; }
  return P[0]+(P[1]-P[1]/2);
}

size_t solve3(const vector<size_t> & A) {
  size_t P[3] = {};
  for (auto x : A) { P[x%3]++; }
  size_t res = P[0];
  size_t o = P[1], t = P[2];
  size_t mn = min(o,t);
  res += mn;
  o -= mn;
  t -= mn;
  res += o/3 + !!(o%3);
  res += t/3 + !!(t%3);
  return res;
}

int dp[111][111][111];

size_t rec(size_t o, size_t t, size_t tt) {
  if (dp[o][t][tt] != -1) return dp[o][t][tt];
  size_t res = 1;
  for (size_t i = 0; i <= 4; i++) {
    for (size_t j = 0; j <= 4; j++) {
      for (size_t k = 0; k <= 4; k++) {
        if (i+j+k > 0 && (i+j*2+k*3)%4 == 0 && o >= i && t >= j && tt >= k) {
          res = max(res, rec(o-i, t-j, tt-k)+1);
        }
      }
    }
  }
  return dp[o][t][tt] = (int)res;
}

size_t solve4(const vector<size_t> & A) {
  size_t P[4] = {};
  for (auto x : A) { P[x%4]++; }
  size_t o = P[1], t = P[2], tt = P[3];
  return P[0] + rec(o, t, tt);
}

int main(void) {
  memset(dp, 255, sizeof(dp));
  dp[0][0][0] = 0;
  size_t T;
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    size_t n,p;
    vector<size_t> A;
    cin >> n >> p;
    A.resize(n);
    for (size_t i = 0; i < n; i++) {
      cin >> A[i];
    }
    cout << "Case #" << tt+1 << ": ";
    if (p == 2) {
      cout << solve2(A) << endl;
    } else if (p == 3) {
      cout << solve3(A) << endl;
    } else if (p == 4) {
      cout << solve4(A) << endl;
    } else {
      assert(0);
    }
  }
  return 0;
}
