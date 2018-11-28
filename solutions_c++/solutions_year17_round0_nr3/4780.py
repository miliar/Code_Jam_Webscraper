#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
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

void solve() {
  int n, k; cin >> n >> k;
  priority_queue<int> heap;
  heap.push(n);
  int mn, mx;
  while (k--) {
    int len = heap.top();
    heap.pop();
    mx = len / 2;
    mn = len - mx - 1;
    heap.push(mx);
    heap.push(mn);
    if (len <= 1) break;
  }
  cout << mx << ' ' << mn;
}

int main() {
  ios_base::sync_with_stdio(false);
  int tt; cin >> tt;
  for (int t = 1; t <= tt; t++) {
    cout << "Case #" << t << ": ";
    solve();
    cout << '\n';
  }
}
