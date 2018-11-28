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


int q[10];

void Solve() {
  int n, p;
  cin >> n >> p;
  memset(q, 0, sizeof q);
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    q[x % p]++;
  }
  int ans = 0;
  ans += q[0];
  if (p == 2) {
    ans += (q[1] + 1) / 2;
  } else if (p == 3) {
    int v = min(q[1], q[2]);
    ans += v;
    q[1] -= v;
    q[2] -= v;
    ans += q[1] / 3;
    ans += q[2] / 3;
    q[1] %= 3;
    q[2] %= 3;
    if (q[1] || q[2]) {
      ++ans;
    }
  } else if (p == 4) {
    int v = min(q[1], q[3]);
    ans += v;
    q[1] -= v;
    q[3] -= v;
    ans += q[2] / 2;
    q[2] %= 2;
    if (q[2]) {
      if (q[1] >= 2) {
        q[2] = 0;
        q[1] -= 2;
        ++ans;
      }
      if (q[3] >= 2) {
        q[2] = 0;
        q[3] -= 2;
        ++ans;
      }
    }
    ans += q[1] / 4;
    ans += q[3] / 4;
    q[1] %= 4;
    q[3] %= 4;
    if (q[1] || q[2] || q[3]) {
      ++ans;
    }
  }
  cout << ans << endl;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
