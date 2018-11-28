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

ll f(ll n, ll k) {
  map<ll, ll> mp;
  mp.insert(pll(n, 1));
  while (true) {
    pll top = *mp.rbegin();
    mp.erase(top.first);
    k -= top.second;
    if (k <= 0) {
      return top.first;
    } else {
      mp[top.first / 2] += top.second;
      mp[(top.first - 1) / 2] += top.second;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  int l;
  cin >> l;
  FOR(t, 1, l + 1) {
    ll n, k;
    cin >> n >> k;
    ll r = f(n, k);
    cout << "Case #" << t << ": " << r / 2 << " " << (r - 1) / 2 << endl;
  }
  return 0;
}
