#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <queue>
#include <deque>
#include <cstring>
#include <iomanip>

using namespace std;

double solve() {
  int n, k;
  double u;
  cin >> n >> k >> u;
  vector<double> p(n);
  for (int i=0;i<n;++i)
    cin >> p[i];
  sort(p.begin(), p.end());
  double cur = 0;
  for (int i=0;i<=n;++i) {
    if (i == n || p[i] > cur) {
      double t = i == n ? 1 : p[i];
      double need = min((t - cur) * i, u);
      u -= need;
      for (int j=0;j<i;++j)
        p[j] += need / i;
      cur = t;
    }
    if (u == 0)
      break;
  }
  double res = 1;
  for (int i=0;i<n;++i) {
    res *= p[i];
  }
  return res;
}

int main() {
#ifdef LOCAL_RUN
  freopen("input.txt", "r", stdin);
#endif
  int t;
  cin >> t;
  for (int i=1;i<=t;++i) {
    printf("Case #%d: %.9f\n", i, solve());
  }
  return 0;
}
