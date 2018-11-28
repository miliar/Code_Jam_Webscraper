#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<ll, ll> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

pii stupid(ll n, ll k) {
  vi c(n + 1);
  c[n] = 1;
  int i = n;
  pii res;
  for (int t = 0; t < k; ++t) {
    while (c[i] == 0) --i;
    --c[i];
    ++c[i/2];
    ++c[(i-1)/2];
    res.first = i/2;
    res.second = (i-1)/2;
  }
  return res;
}

ll f(ll n, ll a, ll b, ll k) {
  if (k <= b) return n;
  k -= b;
  if (k <= a) return n-1;
  k -= a;
  return f(n / 2, a + (n/2 != (n-1)/2 ? a + b : 0), b + (n/2 == (n-1)/2 ? a + b : 0), k);
}

pii solve(ll n, ll k) {
  ll l = f(n, 0, 1, k);
  return pii(l / 2, (l-1) / 2);
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    ll n, k;
    cin >> n >> k;
    pii res = solve(n, k);
    //if (n < 1e8) assert(res == stupid(n, k));
    cout << res.first << ' ' << res.second << endl;
  }
  return 0;
}
