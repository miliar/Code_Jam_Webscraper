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

int d[114];
int pp[114][114];
int now[114];

int prebeg(int p, int k) {
  return (p * 10 - 1) / (k * 11);
}
int las(int p, int k) {
  return p * 10 / (k * 9);
}

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    int n, s;
    cin >> n >> s;
    rep(i, n) {
      cin >> d[i];
    }
    rep(i, n) {
      rep(j, s) {
        cin >> pp[i][j];
      }
      sort(pp[i], pp[i] + s);
    }
    rep(i, n) {
      now[i] = 0;
    }
    int ans = 0;
    while(1) {
      bool en = false;
      rep(i, n) {
        if(now[i] == s) {
          en = true;
          break;
        }
      }
      if(en) {
        break;
      }
      int mi = inf;
      int mip = -1;
      rep(i, n) {
        if(las(pp[i][now[i]], d[i]) < mi) {
          mi = las(pp[i][now[i]], d[i]);
          mip = i;
        }
      }
      bool ok = true;
      rep(i, n) {
        if(mi <= prebeg(pp[i][now[i]], d[i])) {
          ok = false;
          break;
        }
      }
      if(ok) {
        ans++;
        rep(i, n) {
          now[i]++;
        }
      }
      else {
        now[mip]++;
      }
    }
    cout << "Case #" << _ << ": " << ans << endl;
  }
}
