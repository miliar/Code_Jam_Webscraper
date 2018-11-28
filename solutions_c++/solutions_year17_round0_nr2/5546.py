#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

typedef long long LL;

char str[20];
int len;
LL memo[20][10][2];
LL dp(int pos, int prv, bool less) {
  if (pos == len) return 1;
  LL &ret = memo[pos][prv][less];
  if (ret != -1) return ret;
  ret = 0;

  if (less) {
    for (int i = prv; i <= 9; i++) {
      ret += dp(pos + 1, i, true);
    }
  } else {
    int cur = str[pos] - '0';
    for (int i = prv; i <= cur; i++) {
      ret += dp(pos + 1, i, i < cur);
    }
  }
  return ret;
}

LL f(LL val) {
  sprintf(str, "%lld", val);
  len = strlen(str);
  memset(memo, -1, sizeof(memo));
  return dp(0, 0, 0);
}

int t;
LL n;
int main() {
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    cin >> n;
    LL lo = 1, hi = n, mid;
    LL want = f(n);
    while (lo <= hi) {
      mid = (lo + hi) / 2;
      if (f(mid) >= want) hi = mid - 1;
      else lo = mid + 1;
    }
    printf("Case #%d: %lld\n", tc, lo);
  }
  return 0;
}
