#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) (v).begin(), (v).end()
#define eb emplace_back
#define fi first
#define se second

using namespace std;

typedef long long i64;
typedef pair<i64, i64> pii;

void solve() {
  i64 n, k;
  cin >> n >> k;
  map<i64, i64> M;
  M[n] = 1;
  while(true) {
    auto it = M.end(); --it;
    pii q = *it; M.erase(it);
    if (k <= q.se) {
      cout << (q.fi)/2 << ' ' << (q.fi-1)/2 << '\n';
      break;
    }
    k -= q.se;
    M[(q.fi-1)/2] += q.se;
    M[q.fi/2] += q.se;
  }
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
