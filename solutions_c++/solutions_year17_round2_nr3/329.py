#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using ll = long long;
using ld = long double;

template <typename T> T &chmin(T &a, const T &b) { return a = std::min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = std::max(a, b); }
template <typename T> int len(const T &x) { return x.size(); }

struct yes_no : std::numpunct<char> {
  string_type do_truename()  const { return "Yes"; }
  string_type do_falsename() const { return "No"; }
};

void solve();

int main() {
  std::locale loc(std::locale(), new yes_no);
  std::cout << std::boolalpha << std::setprecision(12) << std::fixed;
  std::cout.imbue(loc);
  solve();
  return 0;
}

using namespace std;

void output(const vector<ld> &res) {
  static int c = 0;
  ++c;
  printf("Case #%d:", c);
  for (ld i: res) printf(" %.13Lf", i);
  printf("\n");
}

ld d[128][128];
ld t[128][128];
ld e[128];
ld s[128];

void solve() {
  int T; cin >> T;
  while (T--) {
    // cout << T << endl;
    int n, q;
    cin >> n >> q;
    REP(i,n) cin >> e[i] >> s[i];
    REP(i,n) REP(j,n) {
      cin >> d[i][j];
      if (d[i][j] < -.5) d[i][j] = 1e30;
    }
    REP(k,n) REP(i,n) REP(j,n) chmin(d[i][j], d[i][k] + d[k][j]);
    REP(i,n) REP(j,n) t[i][j] = (d[i][j] <= e[i] + 1e-9 ? d[i][j] / s[i] : 1e30);
    REP(k,n) REP(i,n) REP(j,n) chmin(t[i][j], t[i][k] + t[k][j]);
    // REP(i,n) { REP(j,n) cout << t[i][j] << " "; cout << endl; }
    vector<ld> res;
    REP(i,q) {
      int u, v;
      cin >> u >> v;
      res.push_back(t[u-1][v-1]);
    }
    output(res);
  }
  return;
}
