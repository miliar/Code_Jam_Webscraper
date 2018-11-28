#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cassert>
using namespace std;

#define sz(a) int((a).size())
#define rep(i, s, n)  for(int i = s; i <= (n); ++i)
#define rev(i, n, s)  for(int i = (n); i >= s; --i)
#define fore(x, a) for(auto &&x : a)
typedef long long ll;
const int mod = 1000000007;
const int N = 100005;

int a[22];
ll dp[22][10][2];

ll go(int pos, int prev_digit, bool prefix) {
  if(pos == -1) {
    return 1;
  }
  ll &res = dp[pos][prev_digit][prefix];
  if(res == -1) {
    res = 0;
    rep(i, prev_digit, 9) {
      if(prefix || (prev_digit <= a[pos])) {
        res += go(pos - 1, i, prefix || (prev_digit < a[pos]));
      }
    }
  }
  return res;
}

ll go2(ll n) {
  memset(a, 0, sizeof(a));
  int d = 0;
  while(n > 0) {
    a[d] = n % 10;
    n /= 10;
    d++;
  }
  memset(dp, -1, sizeof(dp));
  return go(21, 0, 0);
}

int main() {
#ifdef loc
  if(!freopen((string(FOLDER) + "inp.txt").c_str(), "r", stdin)) {
    assert(0);
  }
  freopen((string(FOLDER) + "out.txt").c_str(), "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  rep(z, 1, t) {
    cout << "Case #" << z << ": ";
    ll n;
    cin >> n;
    ll tot = go2(n) - 1;
    ll lo = 0, hi = n;
    while(lo < hi) {
      ll mi = (lo + hi) / 2 + 1;
      if(go2(mi) <= tot) {
        lo = mi;
      } else {
        hi = mi - 1;
      }
    }
    cout << lo + 1 << endl;
  }
  return 0;
}