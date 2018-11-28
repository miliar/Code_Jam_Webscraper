#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <numeric>

#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

typedef long long lint;

#define range(i, a, b, step)                                                   \
  for (lint i = (a); i != (lint)(b) && ((i - (lint)(b)) ^ (lint)(step)) < 0;   \
       i += (lint)(step))
#define cache(i, a, b, step)                                                   \
  for (lint i = (a), i##b = (lint)(b), i##step = (lint)(step);                 \
       i != i##b && ((i - i##b) ^ i##step) < 0; i += i##step)

const int maxv = 1002;
const double pi = acos(-1.0);

lint T, k, n, r, h;

struct node {
  lint s, a;

  bool operator<(const node rhs) const {
    if (s == rhs.s)
      return a > rhs.a;
    else
      return s > rhs.s;
  }
} a[maxv];

lint dp[maxv][maxv];

template <typename T> T smin(T a, T b) {
  if (a < b)
    return a;
  else
    return b;
}

template <typename T> T smax(T a, T b) {
  if (a > b)
    return a;
  else
    return b;
}

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  // ios_base::sync_with_stdio(0);
  // cin.tie(0);

  cin >> T;
  range(tcase, 1, T + 1, 1) {
    cin >> k >> n;
    range(i, 0, k, 1) {
      cin >> r >> h;
      a[i].s = r * r;
      a[i].a = r * h * 2;
    }
    sort(a, a + k);
    memset(dp, 0, sizeof(dp));
    dp[0][0] = a[0].s + a[0].a;
    range(i, 1, k, 1) {
      range(j, 0, smin(i + 1, n), 1) {
        if (j == 0)
          dp[i][0] = smax(dp[i - 1][0], a[i].s + a[i].a);
        else
          dp[i][j] = smax(dp[i - 1][j], dp[i - 1][j - 1] + a[i].a);
      }
    }
    printf("Case #%lld: %.10f\n", tcase, dp[k - 1][n - 1] * pi);
  }

  return 0;
}