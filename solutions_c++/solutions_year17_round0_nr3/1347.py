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

#define range(i, a, b, step)                                                   \
  for (long long i = (a);                                                      \
       i != (long long)(b) && ((i - (long long)(b)) ^ (long long)(step)) < 0;  \
       i += (long long)(step))
#define cache(i, a, b, step)                                                   \
  for (long long i = (a), i##b = (long long)(b), i##step = (long long)(step);  \
       i != i##b && ((i - i##b) ^ i##step) < 0; i += i##step)

long long t, n, k;

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> t;
  range(tcase, 1, t + 1, 1) {
    cin >> n >> k;
    long long step = 1;
    while (k > step) {
      k -= step;
      step *= 2;
      n -= step / 2;
    }
    long long ans = n / step;
    if (k <= n % step)
      ans++;
    cout << "Case #" << tcase << ": " << ans / 2 << " " << (ans - 1) / 2
         << endl;
  }

  return 0;
}