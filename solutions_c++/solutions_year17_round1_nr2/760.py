#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n,m;
    cin >> n >> m;
    vvi a(n, vi(m));
    vi r(n);
    for (int i = 0; i < n; ++i) cin >> r[i];
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> a[i][j];
      }
      sort(a[i].begin(), a[i].end());
    }
    vi it(n);
    int res = 0;
    while (true) {
      int mait = 0;
      for (int i = 0; i < n; ++i) mait = max(mait, it[i]);
      if (mait >= m) break;
      int mi = 1e9, ma = 0;
      for (int i = 0; i < n; ++i) {
        int x = a[i][it[i]];
        ma = max(ma, (10 * x + 11 * r[i] - 1) / 11 / r[i]);
        mi = min(mi, 10 * x / 9 / r[i]);
      }
      if (mi >= ma) {
        ++res;
        for (int i = 0; i < n; ++i) ++it[i];
      } else {
        for (int i = 0; i < n; ++i) {
          int x = a[i][it[i]];
          int t = 10 * x / 9 / r[i];
          if (t < ma) ++it[i];
        }
      }
    }
    cout << res << endl;
  }
  return 0;
}
