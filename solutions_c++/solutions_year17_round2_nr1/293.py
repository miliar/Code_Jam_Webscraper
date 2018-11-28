#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

#define sz(x) ((int) (x).size())
#define TASK "text"

const int inf = (int) 1.01e9;
const ld eps = 1e-9;
const ld pi = acos((ld) -1);

mt19937 mrand(random_device{} ()); 

int rnd(int x) {
  return mrand() % x;
}

void precalc() {
}

const int maxn = (int) 1e3 + 5;
int d, n;
pair<int, int> p[maxn];

int read() {
  if (scanf("%d%d", &d, &n) < 2) {
    return false;
  }
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &p[i].first, &p[i].second);
  }
  return true;
}

void solve() {
  sort(p, p + n);
  ld t = 0;
  for (int i = n - 1; i >= 0; i--) {
    t = max(t, (ld) (d - p[i].first) / p[i].second);
  }
  printf("%.12f\n", (double) (d / t));
}

int main() {
  precalc();
#ifdef DEBUG
  assert(freopen(TASK ".in", "r", stdin));
  assert(freopen(TASK ".out", "w", stdout));
#endif
  int t;
  scanf("%d", &t);
  t = 0;
  while (read()) {
    t++;
    printf("Case #%d: ", t);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}
