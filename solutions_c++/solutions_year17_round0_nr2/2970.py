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
deque<int> digits(ll n) {
  deque<int> v;
  while (n) {
    v.push_front(n % 10);
    n /= 10;
  }
  return v;
}
bool isok(ll n) {
  deque<int> v = digits(n);
  REP(i,v.size()-1) if (v[i] > v[i+1]) return false;
  return true;
}
deque<int> solve() {
  ll n;
  cin >> n;

  deque<int> v = digits(n);
  if (isok(n)) return digits(n);

  // find the longest non-decreasing prefix where we can
  // decrease the last digit by 1. then fill out with 9s
  ll q = 10;
  for (int i = v.size()-2; i >= 0; i--, q *= 10) {
    // is this good?
    if (isok(n / q) && (i == 0 || v[i-1] < v[i])) {
      deque<int> a;
      REP(j, i) a.PB(v[j]);
      a.PB(v[i]-1);
      for (int j = i+1; j < v.size(); j++) a.PB(9);
      while (a.size() && a[0] == 0) a.pop_front();
      return a;
    }
  }
  return digits(1);
}

int main() {
   int t;
	 cin >> t;
   REP(qqq, t) {
     cout << "Case #" << (qqq+1) << ": ";
     deque<int> a = solve();
     REP(i, a.size()) cout << a[i]; cout << endl;
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
