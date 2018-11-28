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


const int maxn = (int) 1e3 + 10;
int n, cnt, m;

int bal[maxn];
int men[maxn];

int read() {
  if (scanf("%d%d%d", &n, &cnt, &m) < 3) {
    return 0;
  }
  for (int i = 0; i < n; ++i) {
    bal[i] = 0;
  }
  for (int i = 0; i < cnt; ++i) {
    men[i] = 0;
  }
  for (int i = 0; i < m; ++i) {
    int p, who;
    scanf("%d%d", &p, &who);
    --who;
    --p;
    assert(0 <= who && who < cnt);
    men[who] += 1;
    bal[p] += 1;
  }
  return 1;
}

void solve() {
  int res = *max_element(men, men + cnt);

  int sum = 0;
  for (int i = 0; i < n; ++i) {
    sum += bal[i];
    res = max(res, (sum + i) / (i + 1));
  }

  sum = 0;
  int res2 = 0;
  for (int i = n - 1; i >= 0; --i) {
    sum += bal[i];

    if (bal[i] > res) {
      res2 += (bal[i] - res);
    }
    sum = max(0, sum - res);
  }
  assert(!sum);

  printf("%d %d\n", res, res2);
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
