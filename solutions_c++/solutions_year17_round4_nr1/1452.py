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
#include <sstream>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPF(i, n) for (int i = 0; i <= n; i++)
#define REP2(i, j, n) REP(i, n) for (int j = i+1; j < n; j++)
#define REP3(i, j, k, n) REP2(i, j, n) for (int k = j+1; k < n; k++)
#define CL(x) memset(x, 0, sizeof(x))
#define PB push_back
#define fst first
#define snd second
// typedefs
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double,double> pdd;
// bitset
ll bit(int x) { return ((ll)1)<<x; }
int bitcount(ll x) { return __builtin_popcount(x); }
int bs_count(int x, int i) { return (x & bit(i)) != 0; }
int bs_insert(int x, int i) { return x | bit(i); }
// input
template <typename T> void read(T* a, int n) { REP(i, n) cin >> a[i]; }
// algo
template <typename T> T gcd(T x, T y) { return y ? gcd(y, x % y) : x; }
template <typename T> T ceil(T a, T b) { return (a+b-1)/b; }
// collection
template <typename T> void remove_duplicates(T x) { x.erase(unique(x.begin(), x.end()), x.end()); }
// geom
ll dot(const pll& a, const pll& b) { return a.first*b.first + a.second*b.second; }
ll sq(const pll& a) { return dot(a, a); }
ll cross(pll& a, pll& b) { return a.first*b.second - a.second*b.first; }
pll operator -(const pll& a, const pll& b) { return {a.first - b.first, a.second - b.second}; }
// end

// PUT CODE HERE!!
ll n, p, g, freq[5];
int solve() {
  CL(freq);
  cin >> n >> p;
  REP(i, n) {
    cin >> g;
    freq[g % p]++;
  }

  ll ans = freq[0];

  ll v;
  if (p == 4) {
    // half
    v = freq[2]/2; ans += v; freq[2] -= 2*v;
    v = min(freq[1], freq[3]); ans += v; freq[1] -= v; freq[3] -= v;
    // in three
    if (freq[1]) {
      v = min(freq[1]/2, freq[2]); ans += v; freq[2] -= v; freq[1] -= 2*v;
    }
    if (freq[3]) {
      v = min(freq[3]/2, freq[2]); ans += v; freq[2] -= v; freq[3] -= 2*v;
    }
    // quarters
    v = freq[1]/4; ans += v; freq[1] -= 4*v;
    v = freq[3]/4; ans += v; freq[3] -= 4*v;
  } else if (p == 3) {
    v = min(freq[1], freq[2]); ans += v; freq[1] -= v; freq[2] -= v;
    v = freq[2]/3; ans += v; freq[2] -= 3*v;
    v = freq[1]/3; ans += v; freq[1] -= 3*v;
    //ok
  } else if (p == 2) {
    v = freq[1]/2; ans += v; freq[1] -= 2*v;
    //ok
  }

  if (freq[1] || freq[2] || freq[3]) ans++;

  return ans;
}

int main() {
   int t;
	 cin >> t;
   REP(qqq, t) {
     cout << "Case #" << (qqq+1) << ": " << solve() << endl;
   }
}
