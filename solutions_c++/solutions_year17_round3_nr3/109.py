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
  int n, k;
  cin >> n >> k;
  double u;
  cin >> u;
  vector<double> p(n);
  FOR(i, 0, n) {
    cin >> p[i];
  }
  sort(p.rbegin(), p.rend());

  double mn = 0, mx = 1;
  FOR(rep, 0, 100) {
    double mid = (mn + mx) / 2;
    double r = u;
    FOR(i, 0, k) {
      if (p[i] < mid) {
        r -= mid - p[i];
      }
    }
    if (r < 0) {
      mx = mid;
    } else {
      mn = mid;
    }
  }

  // error(mn);
  // error(mx);

  FOR(i, 0, k) {
    if (p[i] < mx) {
      u -= mx - p[i];
      p[i] = mx;
    }
  }

  // FOR(i, 0, n) {
  //   cout << p[i] << " ";
  // }
  // cout << endl;

  vector<vector<double > > dp(n + 1, vector<double>(n + 1, 0));

  FOR(i, 0, n + 1) {
    dp[i][0] = 1;
  }

  FOR(i, 1, n + 1) {
    FOR(j, 1, n + 1) {
      dp[i][j] = p[i - 1] * dp[i - 1][j - 1] + (1 - p[i - 1]) * dp[i - 1][j];
    }
  }

  cout << fixed << setprecision(8);
  cout << "Case #" << tc << ": ";
  cout << dp[n][k];
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  FOR(l, 1, t + 1) {
    solve(l);
  }
  return 0;
}
