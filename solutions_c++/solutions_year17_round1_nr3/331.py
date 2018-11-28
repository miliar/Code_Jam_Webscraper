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

struct node {
  int hd, ad, hk, ak;
  node(int _hd, int _ad, int _hk, int _ak) {
    hd = _hd;
    ad = _ad;
    hk = _hk;
    ak = _ak;
  }
  bool operator <(const node& A) const{
    if (hd != A.hd) return hd < A.hd;
    if (ad != A.ad) return ad < A.ad;
    if (hk != A.hk) return hk < A.hk;
    if (ak != A.ak) return ak < A.ak;
    return false;
  }
};

// PUT CODE HERE!!
const int INF = 10000000;
int ghd;
int solve(int hd, int ad, int hk, int ak, int b, int d) {
  queue<node> q;
  map<node,int> dist;

  node z = node(hd,ad,hk,ak);
  q.push(z);
  dist[z] = 0;

  //cout << endl;
  while (!q.empty()) {
    node from = q.front(); q.pop();

    hd = from.hd;
    ad = from.ad;
    hk = from.hk;
    ak = from.ak;
    //cout << dist[from] << " " << hd << " " << ad << " "
    //  << hk << " " << ak << endl;

    // attack
    if (hk <= ad) {
      // DIE
      return dist[from] + 1;
    } else {
      node za = node(hd - ak, ad, hk - ad, ak);
      if (za.hd > 0 && dist.count(za) == 0) {
        dist[za] = dist[from]+1;
        q.push(za);
      }
    }

    // buff
      node zb = node(hd - ak, ad + b, hk, ak);
      if (zb.hd > 0 && dist.count(zb) == 0) {
        dist[zb] = dist[from]+1;
        q.push(zb);
      }

    // cure
      node zc = node(ghd - ak, ad, hk, ak);
      if (zc.hd > 0 && dist.count(zc) == 0) {
        dist[zc] = dist[from]+1;
        q.push(zc);
      }

    // debuff
      node zd = node(hd - max(0, ak - d), ad, hk, max(0, ak - d));
      if (zd.hd > 0 && dist.count(zd) == 0) {
        dist[zd] = dist[from]+1;
        q.push(zd);
      }
  }

  // solve
  return INF;
}

int hd, ad, hk, ak, b, d;
void solve() {
  cin >> hd >> ad >> hk >> ak >> b >> d;
  ghd = hd;
  int z = solve(hd, ad, hk, ak, b, d);
  if (z == INF) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << z << endl;
  }
}

int main() {
   int t;
	 cin >> t;
   REP(qqq, t) {
     cout << "Case #" << (qqq+1) << ": ";
     solve();
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
