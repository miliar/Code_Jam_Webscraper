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
int solve() {
  string s; int k;
  cin >> s >> k;
  int ans = 0;
  REP(i, s.size()-k+1) {
    if (s[i] == '-') {
      // flip
      ans++;
      REP(j, k) s[i+j] = (s[i+j] == '-') ? '+' : '-';
    }
  }
  for (int i = s.size()-k+1; i < s.size(); i++) if (s[i] == '-') return -1;
  return ans;
}

int main() {
   int t;
	 cin >> t;
   REP(qqq, t) {
     int a = solve();
     cout << "Case #" << (qqq+1) << ": ";
     if (a == -1)
      cout << "IMPOSSIBLE";
     else
      cout << a;
     cout << endl;
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
