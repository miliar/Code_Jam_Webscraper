#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef long double ld;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;
//typedef long long int;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n, m;
    cin >> n >> m;
    vi t(24 * 60);
//    vi s(n+m), e(n+m);
    for (int i = 0; i < n; ++i) {
      int s,e;
      cin >> s >> e;
      for (int j = s; j < e; ++j) t[j] = 1;
    }
    for (int i = 0; i < m; ++i) {
      int s,e;
      cin >> s >> e;
      for (int j = s; j < e; ++j) t[j] = 2;
    }
    int res = 1e9;
    for (int s = 0; s < 2; ++s) {
      vector<vvi> d(2, vvi(t.size()+1, vi(721, 1e9)));
      d[s][0][0] = 0;
      for (int i = 0; i < t.size(); ++i) {
        for (int p = 0; p < 2; ++p) {
          if (t[i] && t[i] != p + 1) continue;
          for (int x = 1; x <= min(720, i + 1); ++x) {
            d[p][i+1][x] = min(d[p][i+1][x], d[p][i][x-1]);
            d[p][i+1][x] = min(d[p][i+1][x], 1 + d[1-p][i][i - x + 1]);
          }
        }
      }
      res = min(res, d[s][t.size()][720]);
      res = min(res, 1+d[1-s][t.size()][720]);
    }
    cout << res << endl;
  }
  return 0;
}
