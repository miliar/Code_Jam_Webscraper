#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl

#define SIZE(a) ((int) a.size())

typedef long long ll;

typedef pair<int, int> pii;

map<ll, ll> f;

pair<ll, ll> solve(ll n, ll k) {
  f.clear();
  f[n] = 1;

  while (k > 0) {
    ll a = f.rbegin()->first;
    ll cnt = min(f[a], k);

    ll a1 = (a - 1) / 2, a2 = a / 2;
    f[a1] = f[a1] + cnt;
    f[a2] = f[a2] + cnt;

    f[a] = f[a] - cnt;
    k -= cnt;

    if (k == 0) {
      return make_pair(a1, a2);
    }

    if (f[a] == 0) {
      f.erase(f.find(a));
    }
  }

  throw "some thing wrong!";
}

int main() {
  int t;
  cin >> t;

  FOR (i, 1, t) {
    ll n, k;
    cin >> n >> k;
    pair<ll, ll> res = solve(n, k);
    cout << "Case #" << i << ": " << res.second << " " << res.first << endl;
  }

  return 0;
}
