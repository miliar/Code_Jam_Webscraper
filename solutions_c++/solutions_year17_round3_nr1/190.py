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

pair<LL, LL> c[1000];
LL arr[1000];
void solve() {
  int n, k; cin >> n >> k;
  for (int i = 0; i < n; i++) {
    int r, h; cin >> r >> h;
    c[i].first = (2ll * r) * h;
    c[i].second = (1ll * r) * r;
  }
  LL ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) arr[j] = c[j].first;
    arr[i] += c[i].second;
    sort(arr, arr + n);
    LL curr = 0;
    for (int j = 0; j < k; j++) {
      curr += arr[n - j - 1];
    }
    ans = max(ans, curr);
  }
  double res = acos(-1) * ans;
  cout << res << '\n';
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
