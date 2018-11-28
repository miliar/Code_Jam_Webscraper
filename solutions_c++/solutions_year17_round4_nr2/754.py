#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define maximize(a, b) ((a)<(b)?(a)=(b),1:0)
#define minimize(a, b) ((a)>(b)?(a)=(b),1:0)

void input();
void solve(int cs);

int main(int argc, char* argv[]) {
  if (argc == 1) freopen("input.txt", "r", stdin);
  int tc;
  cin >> tc;
  int l = 1, r = tc;
  if (argc > 1) {
    freopen(argv[2], "w", stdout);
    int n = atoi(argv[1]), i = atoi(argv[2]);
    l = tc / n * i + 1;
    r = i+1<n ? tc/n*(i+1) : tc;
  }
  for (int cs = 1; cs <= tc; cs++) {
    input();
    if (cs >= l && cs <= r) solve(cs);
  }
  return 0;
}

const int N = 1024;
int n, c, m;
array<set<int>, N> in;
array<int, N> sz;
array<pair<int, int>, N> x;

pair<bool, int> ok(int md) {
  REP(i, md) sz[i] = n, in[i].clear();
  int res = 0;
  for (int t = 0; t < m; t++) {
    auto a = x[t];
    int mx = 0, i;
    REP(j, md) if (in[j].count(a.se) == 0) {
      if (maximize(mx, sz[j])) i = j;
    }
//    cout << a.fi << " " << mx << endl;
    if (mx == 0) return make_pair(false, 0);
    in[i].insert(a.se);
    if (sz[i] < a.fi) res++;
    sz[i] = min(sz[i]-1, a.fi - 1);
  }
  return make_pair(true, res);
}

void input() {
  cin >> n >> c >> m;
  REP(i, m) cin >> x[i].fi >> x[i].se;
}

void solve(int cs) {
  cout << "Case #" << cs << ": ";
  sort(x.begin(), x.begin() + m);
  reverse(x.begin(), x.begin() + m);

  //ok(1); exit(0);
  int l = 1, r = m;
  while (l < r) {
    int md = (l + r) >> 1;
    if (ok(md).fi) r = md;
    else l = md + 1;
  }
  cout << l << " " << ok(l).se << endl;
}

