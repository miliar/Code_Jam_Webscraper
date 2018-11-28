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

size_t D[111][111];
size_t E[111], S[111];
size_t n;
size_t dpp[111][111];

double find_way(size_t s, size_t t) {
  double dp[111];
  bool u[111] = {};
  for (size_t i = 0; i < n; i++) { dp[i] = 1e100; }
  dp[s] = 0.0;
  u[s] = 1;
  queue<size_t> Q;
  Q.push(s);
  while (Q.size()) {
    size_t v = Q.front();
    Q.pop();
    u[v] = 0;
    for (size_t i = 0; i < n; i++) {
      double dd = dp[v] + (double)dpp[v][i]/(double)S[v];
      if (dpp[v][i] <= E[v] && dp[i] > dd) {
        if (!u[i]) {
          Q.push(i);
          u[i] = 1;
        }
        dp[i] = dd;
      }
    }
  }
  return dp[t];
}

double find_way_dijk(size_t s, size_t t) {
  double dp[111];
  for (size_t i = 0; i < n; i++) { dp[i] = 1e100; }
  dp[s] = 0.0;
  priority_queue<pair<double,size_t>> Q;
  Q.push({0,s});
  while (Q.size()) {
    size_t v = Q.top().second;
    Q.pop();
    for (size_t i = 0; i < n; i++) {
      double dd = dp[v] + (double)dpp[v][i]/(double)S[v];
      if (dpp[v][i] <= E[v] && dp[i] > dd) {
        Q.push({-dd,i});
        dp[i] = dd;
      }
    }
  }
  return dp[t];
}

int main(void) {
  size_t T;
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    size_t q;
    cin >> n >> q;
    for (size_t i = 0; i < n; i++) {
      cin >> E[i] >> S[i];
    }
    for (size_t i = 0; i < n; i++) {
      for (size_t j = 0; j < n; j++) {
        cin >> D[i][j];
        dpp[i][j] = D[i][j];
        if (dpp[i][j] > 1000000000) dpp[i][j] = 2000000000;
      }
      dpp[i][i] = 0;
    }
    for (size_t k = 0; k < n; k++) {
      for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
          dpp[i][j] = min(dpp[i][j], dpp[i][k] + dpp[k][j]);
        }
      }
    }
    cout << "Case #" << tt+1 << ": ";
    for (size_t i = 0; i < q; i++) {
      size_t s,t;
      cin >> s >> t;
      s--,t--;
      cout << fixed << setprecision(10) << find_way(s,t);
      // cout << fixed << setprecision(10) << find_way_dijk(s,t);
      if (i+1 < q) cout << ' ';
    }
    cout << endl;
  }
  return 0;
}
