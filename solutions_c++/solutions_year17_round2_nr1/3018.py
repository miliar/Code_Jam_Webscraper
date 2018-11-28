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
  for (int i = (a); i != (int)(b) && ((i - (int)(b)) ^ (int)(step)) < 0;       \
       i += (int)(step))
#define cache(i, a, b, step)                                                   \
  for (int i = (a), i##b = (int)(b), i##step = (int)(step);                    \
       i != i##b && ((i - i##b) ^ i##step) < 0; i += i##step)

const int maxv = 1002;

int tcase, d, n, k[maxv], s[maxv], a[maxv];

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> tcase;
  range(icase, 0, tcase, 1) {
    cin >> d >> n;
    range(i, 0, n, 1) a[i] = i;
    double slow = 0;
    range(i, 0, n, 1) {
      cin >> k[i] >> s[i];
      slow = max(slow, (d - k[i]) * 1.0 / s[i]);
    }

    printf("Case #%d: %.6f\n", icase + 1, d * 1.0 / slow);
  }

  return 0;
}