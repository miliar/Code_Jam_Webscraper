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


const int maxn = 110;
const int maxp = 4;
int cnt[maxp];

int n, p;

int read() {
  if (scanf("%d%d", &n, &p) < 2) {
    return 0;
  }
  memset(cnt, 0, sizeof(cnt));
  for (int i = 0; i < n; ++i) {
    int x;
    scanf("%d", &x);
    cnt[x % p] += 1;
  }
  return 1;
}

int dp[maxn][maxn][maxn];

void solve() {
  memset(dp, -1, sizeof(dp));
  dp[0][0][0] = 0;

  for (int iter = 0; iter < n; ++iter) {
    for (int a = 0; a <= iter; ++a) {
      for (int b = 0; a + b <= iter; ++b) {
        for (int c = 0; a + b + c <= iter; ++c) {
          auto cur = dp[a][b][c];
          if (cur < 0) {
            continue;
          }

          dp[a][b][c] = -1;
          int vs[] = {a, b, c, iter - a - b - c};
          int sum = (b + 2 * c + 3 * vs[3]) % p;

          for (int i = 0; i < p; ++i) {
            if (vs[i] >= cnt[i]) {
              continue;
            }
            ++vs[i];
            auto &toup = dp[vs[0]][vs[1]][vs[2]];
            toup = max(toup, cur + !sum);
            --vs[i];
          }
        }
      }
    }
  }

  printf("%d\n", dp[cnt[0]][cnt[1]][cnt[2]]);
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
