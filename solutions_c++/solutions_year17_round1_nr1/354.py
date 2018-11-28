#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1000000007LL

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

string d[114];

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    int n, m;
    cin >> n >> m;
    rep(i, n) {
      cin >> d[i];
      char s = '?';
      rep(j, m) {
        if(d[i][j] != '?') {
          s = d[i][j];
        }
        d[i][j] = s;
      }
      rrep(j, m) {
        if(d[i][j] != '?') {
          s = d[i][j];
        }
        d[i][j] = s;
      }
    }
    rep(j, m) {
      char s = '?';
      rep(i, n) {
        if(d[i][j] != '?') {
          s = d[i][j];
        }
        d[i][j] = s;
      }
      rrep(i, n) {
        if(d[i][j] != '?') {
          s = d[i][j];
        }
        d[i][j] = s;
      }
    }
    cout << "Case #" << _ << ":" << endl;
    rep(i, n) {
      cout << d[i] << endl;
    }
  }
}
