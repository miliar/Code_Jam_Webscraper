#ifdef DEBUG
//#define _GLIBCXX_DEBUG
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

const int maxn = 1000;

int n, p;
int g[maxn];

bool read() {
  if (scanf("%d%d", &n, &p) < 2) {
    return false;
  }
  for (int i = 0; i < n; i++) {
    scanf("%d", g + i);
  }
  return true;
}

int cnt[4];
vector<vector<int> > patterns;

vector<int> cur;

void dfs(int pos, int left) {
  if (pos == p) {
    int sum = 0;
    int cnt = 0;
    assert(sz(cur) == p);
    for (int i = 0; i < sz(cur); i++) {
      sum += i * cur[i];
      cnt += cur[i];
    }
    if (!cnt) {
      return;
    }
    if (sum % p == 0) {
      patterns.pb(cur);
    }
    return;
  }
  for (int i = 0; i <= left; i++) {
    cur.pb(i);
    dfs(pos + 1, left - i);
    cur.pop_back();
  }
}

const int maxdp = 1e8;

int dp[maxdp];

int getid(const vector<int> & v) {
  int id = 0;
  for (int i = 0; i < sz(v); i++) {
    id *= cnt[i] + 1;
    id += v[i];
  }
  assert(id < maxdp);
  return id;
}

int mx;

void calcdp(int pos) {
  if (pos == p) {
    int curid = getid(cur);
    int &curdp = dp[curid];
    curdp = 0;
    for (auto &v : patterns) {
      auto now = cur;
      bool ok = true;
      for (int i = 0; i < p; i++) {
        now[i] -= v[i];
        if (now[i] < 0) {
          ok = false;
          break;
        }
      }
      if (ok) {
        int nowid = getid(now);
        curdp = max(curdp, 1 + dp[nowid]);
      }
    }
    mx = max(mx, curdp);
    return;
  }
  for (int i = 0; i <= cnt[pos]; i++) {
    cur.pb(i);
    calcdp(pos + 1);
    cur.pop_back();
  }
}

void solve() {
  memset(cnt, 0, sizeof(cnt));
  for (int i = 0; i < n; i++) {
    cnt[g[i] % p]++;
  }
  patterns.clear();
  dfs(0, p);
  mx = 0;
  calcdp(0);
  int sum = 0;
  for (int i = 0; i < n; i++) {
    sum += g[i];
  }
  if (sum % p == 0) {
    mx--;
  }
  printf("%d\n", mx + 1);
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

