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
  vector<pll> p(n);
  FOR(i, 0, n) {
    cin >> p[i].first >> p[i].second;
  }
  sort(p.rbegin(), p.rend());

  ll best = 0;
  while (Size(p) >= k) {
    vector<ll> c;
    FOR(i, 1, Size(p)) {
      c.pb(2 * p[i].first * p[i].second);
    }
    sort(c.rbegin(), c.rend());
    ll total = p[0].first * p[0].first + 2 * p[0].first * p[0].second;
    FOR(i, 0, k - 1) {
      total += c[i];
    }
    smax(best, total);
    p.erase(p.begin());
  }

  cout << fixed << setprecision(8);
  cout << "Case #" << tc << ": ";
  cout << best * M_PI;
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
