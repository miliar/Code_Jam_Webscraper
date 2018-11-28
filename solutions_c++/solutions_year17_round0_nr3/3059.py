#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <functional>
#include <queue>
#include <cassert>
#include <cstring>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPF(i, n) for (int i = 0; i <= n; i++)
#define REP2(i, j, n) REP(i, n) for (int j = i+1; j < n; j++)
#define REP3(i, j, k, n) REP2(i, j, n) for (int k = j+1; k < n; k++)
#define CL(x) memset(x, 0, sizeof(x))
#define PB push_back
typedef long long ll;
// dp
template <typename T> bool chkmin(T &a, T b) { return a > b ? a = b, true : false; }
template <typename T> bool chkmax(T &a, T b) { return a < b ? a = b, true : false; }
// bitset
ll bit(int x) { return ((ll)1)<<x; }
int bitcount(ll x) { return __builtin_popcount(x); }
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double,double> pdd;
// input
template <typename T> void read(T* a, int n) { REP(i, n) cin >> a[i]; }
// algo
template <typename T> T gcd(T x, T y) { return y ? gcd(y, x % y) : x; }
template <int MOD> ll bigpow(ll x, ll n);
template <typename T> T binary_search_max(T low, T high, function<bool(T)> check);
// collection
template <typename T> void remove_duplicates(T x) { x.erase(unique(x.begin(), x.end()), x.end()); }
// ds
// geom
ll sq(const pll& a) { return a.first*a.first + a.second*a.second; }
ll cross(pll& a, pll& b) { return a.first*b.second - a.second*b.first; }
pll operator -(const pll& a, const pll& b) {
    return {a.first - b.first, a.second - b.second};
}
// end

// PUT CODE HERE!!
pll solve() {
  ll n, k;
  cin >> n >> k;
  map<ll,ll> s;
  pll a = {-1, -1};

  s[n]++;
  while (k > 0) {
    pair<ll,ll> z = (*s.rbegin());

    //cout << z.first << " " << z.second << endl;
    ll take = min(k, z.second);
    k -= take;
    s[z.first] -= take;
    if (s[z.first] == 0) s.erase(s.find(z.first));
    if (z.first % 2 == 1) {
      ll r = (z.first-1)/2;
      if (r) s[r] += 2*take;
      a = {r, r};
    } else {
      ll r1 = z.first/2;
      if (r1) s[r1] += take;

      ll r2 = z.first/2-1;
      if (r2) s[r2] += take;
      a = {r1, r2};
    }
  }

  return a;
}

int main() {
   int t;
	 cin >> t;
   REP(qqq, t) {
     pll a = solve();
     cout << "Case #" << (qqq+1) << ": ";
     cout << a.first << " " << a.second << endl;
   }
}

// helper
template <int MOD> ll bigpow(ll x, ll n) {
  ll r = 1;
  while (n) {
    if (n % 2) r = (r * x) % MOD;
    x = (x * x) % MOD;
    n /= 2;
  }
  return r;
}
template <typename T> T binary_search_max(T low, T high, function<bool(T)> check) {
	while (low < high) {
		T mid = (high+low+1)/2;
		if (check(mid)) {
			low = mid;
		} else {
			high = mid-1;
		}
	}
	return low;
}
