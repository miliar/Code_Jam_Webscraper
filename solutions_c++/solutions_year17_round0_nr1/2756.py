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

const int maxn = 1e4;
int n, k;
char s[maxn];

bool read() {
  if (scanf("%s%d", s, &k) < 2) {
    return false;
  }
  n = strlen(s);
  return true;
}

int dp[maxn];

void solve() {
  memset(dp, 0, sizeof(dp));
  int res = 0;
  for (int i = 0, cur = 0; i < n; i++) {
    if (i >= k) {
      cur ^= dp[i - k];
    }
    int a = (s[i] == '-');
    a ^= cur;
    if (a) {
      if (i + k <= n) {
        res++;
        cur ^= 1;
        dp[i] ^= 1;
      } else {
        printf("IMPOSSIBLE\n");
        return;
      }
    }
  }
  printf("%d\n", res);
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

