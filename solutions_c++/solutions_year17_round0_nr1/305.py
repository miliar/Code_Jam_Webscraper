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

const int maxn = 1005;
int n, k;
string s;
char tmp[maxn];

int read() {
  if (scanf("%s%d", tmp, &k) < 1) {
    return false;
  }
  s = tmp;
  n = sz(s);
  return true;
}

void solve() {
  int res = 0;
  for (int i = 0; i < n; i++) {
    if (s[i] == '-') {
      if (i + k > n) {
        printf("IMPOSSIBLE\n");
        return;
      }
      res++;
      for (int j = i; j < i + k; j++) {
        if (s[j] == '-') {
          s[j] = '+';
        } else {
          s[j] = '-';
        }
      }
    }
  }
  printf("%d\n", res);
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
