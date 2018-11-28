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

typedef pair<int, char> cf;

pair<bool, string> solve_easy(int rc, int bc, int yc) {
  vector<cf> v;
  v.pb(cf(rc, 'R'));
  v.pb(cf(bc, 'B'));
  v.pb(cf(yc, 'Y'));
  sort(all(v));
  
  if (v[0].first + v[1].first < v[2].first) {
    return make_pair(false, "");
  }

  string one;
  FOR(i, 0, v[2].first) {
    one += v[2].second;
    if (v[1].first) {
      one += v[1].second;
      v[1].first--;
    } else {
      one += v[0].second;
      v[0].first--;
    }
  }

  // cout << "ONE " << one << endl;

  assert(v[1].first == 0);

  string two;
  FOR(i, 0, Size(one)) {
    two += one[i];
    if (v[0].first) {
      two += v[0].second;
      v[0].first--;
    }
  }

  assert(Size(two) == rc + bc + yc);

  return make_pair(true, two);
}

void solve(int tc) {
  int n, r, o, y, g, b, v;
  cin >> n >> r >> o >> y >> g >> b >> v;
  
  pair<bool, string> result = solve_easy(r, b, y);

  bool possible = result.first;
  string str = result.second;

  if (possible) {
    assert(count(all(str), 'R') == r);
    assert(count(all(str), 'O') == o);
    assert(count(all(str), 'Y') == y);
    assert(count(all(str), 'G') == g);
    assert(count(all(str), 'B') == b);
    assert(count(all(str), 'V') == v);
    FOR(i, 0, Size(str)) {
      assert(str[i] != str[(i + 1) % Size(str)]);
    }
  }

  cout << "Case #" << tc << ": ";
  cout << (possible ? str : "IMPOSSIBLE");
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
