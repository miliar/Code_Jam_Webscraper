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
#include <cassert>

const double INF = 1e10, INF2 = 1e9;

using namespace std;

double solve() {
  int d, n;
  cin >> d >> n;
  double res = 1e100;
  for (int i=0;i<n;++i) {
    int k, s;
    cin >> k >> s;
    double t = 1.0 * (d - k) / s;
    res = min(res, (k + s * t) / t);
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
    printf("Case #%d: %.10f\n", i, solve());
  }
  return 0;
}