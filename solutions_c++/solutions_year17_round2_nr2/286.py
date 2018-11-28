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

const int k = 6;
char s[k + 1] = "ROYGBV";

int n;
int a[k];

bool read() {
  if (scanf("%d", &n) < 1) {
    return false;
  }
  for (int i = 0; i < k; i++) {
    scanf("%d", a + i);
  }
  return true;
}

void solve() {
  vector<vector<string> > v(6);
  for (int i = 0; i < 6; i++) {
    for (int j = 0; j < a[i]; j++) {
      char tmp[2];
      tmp[0] = s[i];
      tmp[1] = 0;
      v[i].pb(string(tmp));
    }
  }
  for (int c1 = 1; c1 <= 5; c1 += 2) {
    for (auto i : v[c1]) {
      int diam = (c1 + 3) % 6;
      if (sz(v[diam]) < 2) {
        if (sz(v[diam]) == 1) {
          bool ok = true;
          for (int j = 0; j < k; j++) {
            if (j == c1 || j == diam) {
              continue;
            }
            if (sz(v[j])) {
              ok = false;
              break;
            }
          }
          if (ok) {
            string cur = (i + v[diam][0]);
            printf("%s\n", cur.c_str());
            return;
          }
        }
        printf("IMPOSSIBLE\n");
        return;
      }
      string cur = v[diam].back();
      v[diam].pop_back();
      cur += i;
      cur += v[diam].back();
      v[diam].pop_back();
      v[diam].pb(cur);
    }
    v[c1].clear();
  }
  int sum = 0;
  for (int i = 0; i < 6; i++) {
    sum += sz(v[i]);
  }
  for (int i = 0; i < 6; i++) {
    if (sum < 2 * sz(v[i])) {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  for (int i = 0; i < 6; i++) {
    if (sz(v[i]) > sz(v[0])) {
      swap(v[i], v[0]);
    }
  }
  vector<string> ans(sum);
  int pos = 0;
  for (int i = 0; i < 6; i++) {
    for (auto &j : v[i]) {
      ans[pos] = j;
      pos += 2;
      if (pos >= sum) {
        pos -= sum;
        if (!(pos & 1)) {
          pos++;
        }
      }
    }
  }
  for (auto toprint : ans) {
    printf("%s", toprint.c_str());
  }
  printf("\n");
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

