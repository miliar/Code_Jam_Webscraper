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
ll ceil(ll a, ll b) {
  return (a+b-1)/b;
}
ll compute_low(ll r, ll q) {
  return ceil((10*q),(11*r));
}
ll compute_high(ll r, ll q) {
  return (10*q) / (9*r);
}

const int N = 55, P = 55;
ll n, p, r[N], q[N][P];

const int T = 1000005;
vector<int> up[N][T];
multiset<int> freq[N];
ll solve() {
  cin >> n >> p;
  REP(i, n) cin >> r[i];
  REP(i, n) REP(j, p) cin >> q[i][j];

  CL(up);

  //cout << endl;
  set<int> zz;
  REP(i, n) {
    REP(j, p) {
      ll a = compute_low(r[i], q[i][j]);
      ll b = compute_high(r[i], q[i][j]);
      if (a <= b) {
        up[i][ a ].PB(b);
        zz.insert(a);
        zz.insert(b);
      }
    }
  }

  REP(i, n) freq[i].clear();

  ll ans = 0;
  for (auto tt: zz) {

    REP(i, n)  {
      for (auto q: up[i][tt]) freq[i].insert(q);
    }

    bool flag = false;
    while (!flag) {
      REP(i, n) if (freq[i].empty()) flag = true;
      if (!flag) {
        ans++;
        REP(i, n) {
          freq[i].erase(freq[i].begin());
        }
      }
    }

    REP(i, n) {
      while (!freq[i].empty() && *freq[i].begin() == tt)
        freq[i].erase(freq[i].begin());
    }

  }

  return ans;
}

int main() {
   int t;
	 cin >> t;
   REP(qqq, t) {
     cout << "Case #" << (qqq+1) << ": ";
     ll a = solve();
     cout << a << endl;
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
