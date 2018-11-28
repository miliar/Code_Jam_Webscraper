#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>

using namespace std;

int T, D, N;

int solve() {
  int ans = 0;
  return ans;
}

int main() {
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> D >> N;
    double maxTime = 0.0;
    int k, s;
    for (int j = 1; j <= N; j++) {
      cin >> k >> s;
      double curTime = (D - k) / (double)s;
      maxTime = max(maxTime, curTime);
    }
    //long double ans = ((long double)D * rs) / (long double)(D - rk);
    double ans = D / maxTime;
    //cout << "Case #" << i << ": " << ans << endl;
    printf("Case #%d: %.6f\n", i, ans);
    if (ans < 0) {
      assert(false);
    }
  }
  return 0;
}
