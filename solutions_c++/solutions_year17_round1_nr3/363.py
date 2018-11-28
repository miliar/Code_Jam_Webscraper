#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1000007LL

#define rep(i, n) for(int i = 0; i < (n); i++)
#define rrep(i, n) for(int i = (n) - 1; i >= 0; i--)
#define trep(i, n) for(int i = 0; i <= (n); i++)
#define rep1(i, n) for(int i = 1; i <= (n); i++)
#define mfor(i, s, t) for(int i = (s); i < (t); i++)
#define tfor(i, s, t) for(int i = (s); i <= (t); i++)

class Ford {
public:
  vector<vector<int>> v;
  vector<vector<int>> e;
  vector<bool> used;
  Ford(int n) {
    v.resize(n);
    e.resize(n);
    for(auto& i : e) {
      i.resize(n);
    }
  }
  void add(int f, int t, int c) {
    v[f].push_back(t);
    v[t].push_back(f);
    e[f][t] += c;
  }
  int dfs(int n, int t, int c) {
    if(n == t) {
      return c;
    }
    if(used[n]) {
      return 0;
    }
    used[n] = true;
    for(auto i : v[n]) {
      int w = dfs(i, t, min(c, e[n][i]));
      if(w > 0) {
        e[n][i] -= c;
        e[i][n] += c;
        return w;
      }
    }
    return 0;
  }
  int solve(int b, int e) {
    used.resize(v.size());
    int ans = 0;
    while(1) {
      rep(i, used.size()) {
        used[i] = false;
      }
      int w = dfs(b, e, inf);
      if(w == 0) {
        break;
      }
      ans += w;
    }
    return ans;
  }
};

int need(int t, int s) {
  if((t - 1) % (s - 1) == 0) {
    return (t - 1) / (s - 1) * s;
  }
  else if(t % (s - 1) == 0) {
    return t / (s - 1) * s - 1;
  }
  else {
    return t / (s - 1) * s + t % (s - 1);
  }
}

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    int hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    int as = inf * inf;
    rep(i, inf) {
      as = min(as, i + (hk - 1) / (ad + b * i) + 1);
    }
    int ans = inf * inf;
    int nt = 0;
    int nd = hd;
    rep(i, inf * 2) {
      if(nd <= ak - d) {
        nd = hd;
      }
      else {
        if(ak <= 0) {
          ans = min(ans, i + as);
        }
        else {
          if(as <= (nd - 1) / ak + 1) {
            ans = min(ans, i + as);
          }
          else if((hd - 1) / ak >= 2) {
            int m = (nd - 1) / ak;
            ans = min(ans, i + m + 1 + need(as - m, (hd - 1) / ak));
          }
        }
        if(ak > 0) {
          ak -= d;
        }
      }
      nd -= ak;
    }
    if(ans == inf * inf) {
      cout << "Case #" << _ << ": IMPOSSIBLE" << endl;
    }
    else {
      cout << "Case #" << _ << ": " << ans << endl;
    }
  }
}
