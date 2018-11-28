// TEMPLATE {{{
#include <bits/stdc++.h>
using namespace std;
#ifndef LOCAL
#define OJ 1
#else
#define OJ 0
#endif

#define endl '\n'
#define TIMESTAMP merr << "Execution time: " << (double)clock()/CLOCKS_PER_SEC << " s.\n"
class C_ {}; template <typename T> C_& operator <<(C_& __m, const T& __s) { if (!OJ) cerr << "\E[91m" << __s << "\E[0m"; return __m; }
C_ merr;

struct __s { __s() { if (OJ) { ios_base::Init i; cin.sync_with_stdio(0); cin.tie(0); } } ~__s(){ TIMESTAMP; } } __S;
/// END OF TEMPLATE }}}

#define size_t unsigned long long

size_t n,r,o,y,g,b,v;
string solve() {
  string ans;
  priority_queue<tuple<size_t,size_t,char>> Q;
  for (size_t i = 0; i < r; i++) { Q.push({i,rand(),'R'}); }
  for (size_t i = 0; i < y; i++) { Q.push({i,rand(),'Y'}); }
  for (size_t i = 0; i < b; i++) { Q.push({i,rand(),'B'}); }
  while (Q.size()) {
    vector<tuple<size_t,size_t,char>> buf;
    while (ans.size() > 0 && Q.size() > 0 && get<2>(Q.top()) == ans[ans.size()-1]) {
      buf.push_back(Q.top());
      Q.pop();
    }
    if (Q.size() == 0) {
      return "IMPOSSIBLE";
    }
    ans += get<2>(Q.top());
    Q.pop();
    for (auto x : buf) Q.push(x);
  }
  if (n > 1 && ans[0] == ans[ans.size()-1]) return "IMPOSSIBLE";
  return ans;
}

int main(void) {
  size_t T;
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  srand((int)time(0));
  cin >> T;
  for (size_t tt = 0; tt < T; tt++) {
    cin >> n >> r >> o >> y >> g >> b >> v;
    cout << "Case #" << tt+1 << ": ";
    bool ok = false;
    for (size_t ttt = 0; ttt < 50; ttt++) {
      string ans = solve();
      if (ans != "IMPOSSIBLE") {
        cout << ans << endl;
        ok = true;
        break;
      }
    }
    if (!ok) {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
