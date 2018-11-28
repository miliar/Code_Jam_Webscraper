#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define sz(s) ((int) ((s).size()))

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

typedef long long ll;
typedef long double ld;

const int inf = (int) 1.01e9;
const ld eps = 1e-11;
const ld pi = acos(-1.0L);

mt19937 mrand(random_device{} ());
int rnd(int x) {
  return mrand() % x;
}

const int mod = (int) 1e9 + 7;

void add(int & x, int y) {
  if ((x += y) >= mod) {
    x -= mod;
  }
}

int sum(int x, int y) {
  add(x, y);
  return x;
}

int mult(int x, int y) {
  return (ll) x * y % mod;
}

int power(int x, ll p) {
  int res = 1;
  while (p) {
    if (p & 1) {
      res = mult(res, x);
    }
    x = mult(x, x);
    p >>= 1;
  }
  return res;
}

int inv(int x) {
  return power(x, mod - 2);
}

void precalc() {
}

ll n, k;

bool read() {
  if (scanf("%lld%lld", &n, &k) < 2) {
    return false;
  }
  return true;
}

void solve() {
  map<ll, ll> m;
  m[n] = 1;
  ll a, b;
  while (k) {
    auto it = m.end();
    it--;
    ll cur = it->first;
    ll cnt = it->second;
    if (!cnt) {
      m.erase(it);
      continue;
    }
    ll take = min(cnt, k);
    m[cur] -= take;
    m[(cur - 1) / 2] += take;
    m[cur / 2] += take;
    a = cur / 2;
    b = (cur - 1) / 2;
    k -= take;
  }
  printf("%lld %lld\n", a, b);
}

int main() {
  precalc();
#ifdef DEBUG
  assert(freopen("text.in", "r", stdin));
  assert(freopen("text.out", "w", stdout));
#endif

  int t;
  scanf("%d", &t);
  t = 0;
  while (read()) {
    printf("Case #%d: ", ++t);
    solve();
#ifdef DEBUG
    eprintf("Time: %.3f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}

