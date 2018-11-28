#include <bits/stdc++.h>
using namespace std;

long long pow10[19];
int bits[22];
long long f[111][10][2];

long long dp(int pos, int pre_num, bool upper) {
  if (pos == -1) {
    return 0;
  }
  if (f[pos][pre_num][upper] != -1) {
    return f[pos][pre_num][upper];
  }
  long long &res = f[pos][pre_num][upper];
  res = -1;
  for (int num = pre_num; num <= (!upper ? 9 : bits[pos]); ++num) {
    long long tmp = -1;
    if (num < bits[pos]) {
      tmp = dp(pos-1, num, false);
    } else {
      tmp = dp(pos-1, num, upper);
    }
    if (tmp == -1) {
      continue;
    }
    res = max(res, tmp + pow10[pos] * num);
  }
  return res;
}

int main(void) {

  pow10[0] = 1;
  for (int i = 1; i <= 18; ++i) {
    pow10[i] = pow10[i-1] * 10ll;
  }

  int cases; scanf("%d", &cases);
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d: ", cas);

    long long n; scanf("%lld", &n);
    int len = 0;
    for (long long t = n; t; t /= 10) {
      bits[len++] = t % 10;
    }

    memset(f, -1, sizeof f);
    // printf("%d\n", len);
    printf("%lld\n", dp(len-1, 0, true));

  }

  return 0;
}