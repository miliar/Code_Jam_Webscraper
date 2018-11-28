#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

mt19937 mrand(random_device{} ()); 

int rnd(int x) {
  return mrand() % x;
}

typedef long double ld;
typedef long long ll;

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

#define pb push_back
#define mp make_pair
#define sz(x) ((int) (x).size())
#define TASK "text"

const int inf = (int) 1.01e9;
const ld eps = 1e-9;
const ld pi = acos((ld) -1.0);

const int mod = (int) 1e9 + 7;

void add(int &x, int y) {
  if ((x += y) >= mod) {
    x -= mod;
  }
}

int mult(int x, int y) {
  return (long long) x * y % mod;
}

int power(int x, int pw) {
  int res = 1;
  for (; pw; pw >>= 1) {
    if (pw & 1) {
      res = mult(res, x);
    }
    x = mult(x, x);
  }
  return res;
}

void precalc() {
}


long long n;

int read() {
  if (scanf("%lld", &n) < 1) {
    return 0;
  }
  return 1;
}

void solve() {
  vector<int> a;
  for (auto x = n; x; x /= 10) {
    a.pb(x % 10);
  }
  reverse(a.begin(), a.end());

  int best = 0;
  int pos = 1;
  while (pos < sz(a) && a[pos] >= a[pos - 1]) {
    if (a[pos] > a[pos - 1]) {
      best = pos;
    }
    ++pos;
  }
  if (pos == sz(a)) {
    printf("%lld\n", n);
    return;
  }
  long long ten = 1;
  for (int i = 0; i < sz(a) - best - 1; ++i) {
    ten *= 10;
  }
  n = n - n % ten;
  --n;
  printf("%lld\n", n);
}

int main() {
  precalc();
#ifdef LOCAL
  freopen(TASK ".out", "w", stdout);
  assert(freopen(TASK ".in", "r", stdin));
#endif

  int t;
  scanf("%d", &t);
  t = 0;
  while (1) {
    if (!read()) {
      break;
    }
    printf("Case #%d: ", ++t);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}
