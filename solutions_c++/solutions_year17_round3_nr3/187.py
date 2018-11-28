#include <bits/stdc++.h>
using namespace std;
namespace {
  #ifdef LOCAL_JUDGE
    #define trace(...) cerr << ">> "; __f(#__VA_ARGS__, __VA_ARGS__)
    template <typename Arg1>
    void __f(const char* name, Arg1&& arg1) {
      cerr << name << " = " << arg1 << std::endl;
    }
    template <typename Arg1, typename... Args>
    void __f(const char* names, Arg1&& arg1, Args&&... args) {
      const char* comma = strchr(names + 1, ',');
      cerr.write(names, comma - names) << " = " << arg1<<" | ";__f(comma+1, args...);
    }
    #define debug cerr << ">>> line " << __LINE__ << '\n';
  #else
    #define trace(...)
    #define debug
  #endif
};
typedef long long LL;

const int N = 51;
const double EPS = 1e-10;
double p[N];

void solve() {
  int n, k; cin >> n >> k;
  double u; cin >> u;
  for (int i = 0; i < n; i++) cin >> p[i];

  if (k != n) {
    cout << "error\n";
    return;
  }
  sort(p, p + n);
  p[n] = 2;

  for (int i = 0; i < n; i++) {
    if (u < EPS) break;
    double delta = min(u / (i + 1), p[i + 1] - p[i]);
    // trace(delta);
    for (int j = 0; j <= i; j++) p[j] += delta;
    // cerr << "> "; for (int j = 0; j < n; j++) cerr << p[j] << ' '; cerr << '\n';
    u -= (i + 1) * delta;
  }
  double ans = 1;
  for (int i = 0; i < n; i++) {
    ans *= p[i];
  }
  cout << ans << '\n';
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  cout.precision(10);
  cout << fixed;

  int t; cin >> t;
  for (int it = 1; it <= t; it++) {
    cout << "Case #" << it << ": ";
    solve();
  }
  return 0;
}
