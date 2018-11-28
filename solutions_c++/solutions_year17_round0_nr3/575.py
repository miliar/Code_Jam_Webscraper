#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define cl(x, v) memset((x), (v), sizeof(x))

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef long double ld;

typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const ld EPS = 1e-9, PI = acos(-1.);
const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const int N = 1e5+5;

int t;
ll n, k, mi, ma;

void solve() {
  map<ll, ll> m;
  m[n] = 1;

  auto it = m.end(); it--;
  while (it->nd < k) {
    ll a = it->st - 1;
    ll b = it->nd;
    m.erase(it);

    ll al = a/2, ar = a-al;
    m[al] += b;
    m[ar] += b;

    k -= b;

    it = m.end(); it--;
  }

  ll a = it->st - 1;
  mi = a/2; ma = a-a/2;
}

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt <= t; ++tt) {
    scanf("%lld%lld", &n, &k);
    solve();
    printf("Case #%d: %lld %lld\n", tt, ma, mi);
    fflush(stdout);
  }
  return 0;
}
