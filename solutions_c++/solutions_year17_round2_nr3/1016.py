#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; }
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; }
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

void solve(int tc) {
  int n, q;
  cin >> n >> q;
  vector<int> e(n), s(n);
  FOR(i, 0, n) {
    cin >> e[i] >> s[i];
  }
  vector<vector<ll> > d(n, vector<ll>(n));
  FOR(i, 0, n) {
    FOR(j, 0, n) {
      cin >> d[i][j];
    }
  }
  while (q--) {
    int u, v;
    cin >> u >> v;
  }
  FOR(l, 2, n) {
    FOR(j, l, n) {
      int i = j - l;
      assert(d[i][j - 1] >= 0);
      assert(d[j - 1][j] >= 0);
      // cout << i << " " << j << endl;
      d[i][j] = d[i][j - 1] + d[j - 1][j];
    }
  }
  vector<double> dp(n, -1);
  dp[n - 1] = 0;
  for (int i = n - 2; i >= 0; i--) {
    FOR(j, i + 1, n) {
      if (d[i][j] > e[i]) {
        continue;
      }
      if (dp[j] < -.5) {
        continue;
      }
      double c = dp[j] + 1. * d[i][j] / s[i];
      if (dp[i] < -.5 || c < dp[i]) {
        dp[i] = c;
      }
    }
  }
  cout << fixed << setprecision(8);
  cout << "Case #" << tc << ": ";
  cout << dp[0];
  cout << endl;
  assert(dp[0] > -.5);
}

int main() {
  int t;
  cin >> t;
  FOR(l, 1, t + 1) {
    solve(l);
  }
  return 0;
}
