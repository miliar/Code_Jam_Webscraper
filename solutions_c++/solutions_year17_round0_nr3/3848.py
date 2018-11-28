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

pair<size_t,size_t> getMM(const vector<bool> & u, size_t idx) {
  size_t l = 0, r = 0;
  size_t saved = idx;
  while (idx > 0 && !u[idx-1]) {
    idx--;
    l++;
  }
  idx = saved;
  while (idx+1 < u.size() && !u[idx+1]) {
    idx++;
    r++;
  }
  return {min(l,r),max(l,r)};
}

pair<size_t,size_t> brute(size_t n, size_t k) {
  vector<bool> u(n);
  pair<size_t,size_t> res = {0,0};
  for (size_t tt = 0; tt < k; tt++) {
    pair<size_t,size_t> p = {0,0};
    size_t ai = n+1;
    for (size_t i = 0; i < n; i++) {
      if (u[i]) continue;
      auto pp = getMM(u, i);
      // merr << i+1 << " " << pp.first << " " << pp.second << '\n';
      if (pp > p || (pp == p && ai > i)) {
        ai = i;
        p = pp;
      }
    }
    u[ai] = 1;
    res = p;
  }
  return res;
}

pair<size_t,size_t> cleverer(size_t n, size_t k) {
  priority_queue<size_t> Q;
  Q.push(n);
  for (size_t tt = 0; tt < k-1; tt++) {
    size_t x = Q.top();
    Q.pop();
    if (x > 2) Q.push((x-1)/2);
    if (x > 1) Q.push((x-1)-(x-1)/2);
  }
  size_t res = Q.top();
  return {(res-1)/2, (res-1)-(res-1)/2};
}

int main(void) {
  // for (size_t nn = 1; nn < 1000; nn++) {
    // merr << '\r' << nn << '\r';
    // for (size_t kk = 1; kk <= nn; kk++) {
      // assert(brute(nn, kk) == cleverer(nn, kk));
    // }
  // }
  // return 0;
  // for (size_t i = 1; i < 10000000; i++) {
    // merr << '\r' << i << '\r';
    // assert(to_string(brute(i)) == clever(i));
  // }
  // return 0;
  size_t T;
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    merr << '\r' << tt << '\r';
    size_t n,k;
    cin >> n >> k;
    cout << "Case #" << tt+1 << ": ";
    // auto ans = brute(n, k);
    auto ans = cleverer(n, k);
    cout << ans.second << " " << ans.first << endl;
  }
  return 0;
}
