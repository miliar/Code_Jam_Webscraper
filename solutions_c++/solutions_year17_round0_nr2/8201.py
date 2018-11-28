/*input
4
132
1000
7
111111111111111110
*/
#include <bits/stdc++.h>
using namespace std;

long long solve(long long rem, int prev, long long bs) {
  if (rem < 0) return -1;
  // cout << rem << ' ' << prev << ' ' << bs << endl;
  if (bs == 0) return 0;
  long long ans = -1;
  for (int nexdig = 9; ans == -1 && nexdig >= prev; nexdig--) {
    long long r = bs * nexdig;
    long long a = solve(rem - r, nexdig, bs / 10);
    if (a >= 0)
      ans = r + a;
  }
  return ans;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    long long n;
    scanf("%I64d", &n);
    printf("Case #%d: %I64d\n", tc, solve(n, 0, 1000000000000000000LL));
  }
  return 0;
}