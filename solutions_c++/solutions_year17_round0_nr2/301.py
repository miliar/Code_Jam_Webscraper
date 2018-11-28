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

const int maxn = 25;
int n;
string s;
char tmp[maxn];

int read() {
  if (scanf("%s", tmp) < 1) {
    return false;
  }
  s = tmp;
  n = sz(s);
  return true;
}

bool check(const string &t) {
  for (int i = 0; i + 1 < n; i++) {
    if (t[i + 1] < t[i]) {
      return false;
    }
  }
  return true;
}

void solve() {
  string res;
  if (check(s)) {
    res = s;
  }
  for (int i = 0; i < n; i++) {
    for (char c = '0'; c < s[i]; c++) {
      string t = s;
      t[i] = c;
      for (int j = i + 1; j < n; j++) {
        t[j] = '9';
      }
      if (check(t) && t > res) {
        res = t;
      }
    }
  }
  long long x = 0;
  for (int i = 0; i < n; i++) {
    x = x * 10 + (res[i] - '0');
  }
  printf("%lld\n", x);
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
