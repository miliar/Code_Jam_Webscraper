#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cassert>
using namespace std;

#define sz(a) int((a).size())
#define rep(i, s, n)  for(int i = s; i <= (n); ++i)
#define rev(i, n, s)  for(int i = (n); i >= s; --i)
#define fore(x, a) for(auto &&x : a)
typedef long long ll;
const int mod = 1000000007;
const int N = 105;

ll d[N][N];
ll e[N], s[N];
double dp[N];
bool v[N];
int n;
const double eps = 1e-20;

/*
double go(int x) {
  if (x == n) return 0.0;
  double &res = dp[x];
  if (v[x]) return res;
  res = 1e40;
  v[x] = 1;
  ll tot = 0;
  rep(i, x, n - 1) {
    tot += d[i][i + 1];
    if (tot <= e[x]) {
      res = min(res, go(i + 1) + (tot / (double)s[x]));
    }
  }
  return res;
}
*/

int main() {
#ifdef loc
  if (!freopen((string(FOLDER) + "inp.txt").c_str(), "r", stdin)) {
    assert(0);
  }
  freopen((string(FOLDER) + "out.txt").c_str(), "w", stdout);
#endif
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t;
  cin >> t;
  const ll inf = mod * 1LL * mod;
  rep(z, 1, t) {
    cout << "Case #" << z << ": ";
    int q;
    cin >> n >> q;
    rep(i, 1, n) {
      cin >> e[i] >> s[i];
    }
    rep(i, 1, n) {
      rep(j, 1, n) {
        cin >> d[i][j];
        if (d[i][j] == -1) d[i][j] = inf;
      }
    }
    rep(k, 1, n) {
      rep(i, 1, n) {
        rep(j, 1, n) {
          d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        }
      }
    }
    rep(i, 1, n) {
      rep(j, 1, n) {
        if (d[i][j] >= inf) d[i][j] = -1;
      }
    }
    rep(Q,1,q) {
      int a, b;
      cin >> a >> b;
      rep(i, 1, n) {
        dp[i] = 1e100;
      }
      dp[b] = 0;
      set<pair<double, int>> pq;
      memset(v, 0, sizeof(v));
      pq.insert({ dp[b], b });
      while (!pq.empty()) {
        int x = pq.begin()->second;
        pq.erase(pq.begin());
        if (v[x]) continue;
        v[x] = 1;
        if (x == a) {
          cout << fixed << setprecision(14) << dp[x];
          if (Q == q) cout << '\n';
          else cout << ' ';
          break;
        }
        rep(i, 1, n) {
          if (v[i]) continue;
          if (d[i][x] == -1 || d[i][x] > e[i]) continue;
          if (dp[x] + (d[i][x]) / (double)s[i] + eps< dp[i]) {
            dp[i] = dp[x] + (d[i][x]) / (double)s[i];
            pq.insert({ dp[i],i });
          }
        }
      }
    }
  }
  return 0;
}