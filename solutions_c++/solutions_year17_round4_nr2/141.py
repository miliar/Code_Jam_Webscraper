#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

int needed[1005];
int cust[1005];

void Solve() {
  int n, c, m;
  cin >> n >> c >> m;
  memset(needed, 0, sizeof needed);
  memset(cust, 0, sizeof cust);
  for (int i = 0; i < m; ++i) {
    int x, y;
    cin >> x >> y;
    --x;
    --y;
    cust[y]++;
    needed[x]++;
  }
  int ans = 0, ans2 = 0;
  for (int i = 0; i < c; ++i) {
    ans = max(ans, cust[i]);
  }
  bool failed = true;
  while (failed) {
    failed = false;
    int bal = 0;
    ans2 = 0;
    for (int i = 0; i < n; ++i) {
      bal += ans;
      bal -= needed[i];
      ans2 += max(0, needed[i] - ans);
      if (bal < 0) {
        failed = true;
        ++ans;
        break;
      }
    }
  }
  cout << ans << " " << ans2 << endl;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
