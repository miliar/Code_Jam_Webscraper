#include<bits/stdc++.h>
#define In freopen("E:\\GitHub\\acm\\gcj\\2017\\Qualification Round\\B\\B-large.in", "r", stdin);
#define Out freopen("E:\\GitHub\\acm\\gcj\\2017\\Qualification Round\\B\\solve_out.txt", "w", stdout);
typedef long long LL;

const int maxn = 30;
LL dp[maxn][maxn];

using namespace std;

int cal(LL n) {
  int digit[20];
  LL tn = n;
  int len = 0;
  while (tn > 0) {
    digit[len++] = tn % 10;
    tn /= 10;
  }

  LL ans = 0;
  int lastDigit = 0;
  for (int index = len - 1; index >= 0; index--) {
    for (int d = lastDigit; d < digit[index]; d++) {
      ans += dp[d][index];
    }

    if (digit[index] < lastDigit) {
      return ans;
    }
    lastDigit = digit[index];
  }

  return ans + 1;
}

int main() {
  In
  Out
  for (int d = 1; d <= 9; d++) {
    dp[d][0] = 1;
  }

  for (int l = 1; l <= 18; l++) {
    for (int d = 9; d >= 0; d--) {
      for (int k = d; k < 10; k++) {
        dp[d][l] += dp[k][l-1];
      }
    }
  }

  int T;
  for (int t = scanf("%d", &T); t <= T; t++) {
    LL n;
    scanf("%I64d", &n);
    LL num = cal(n);
    LL l = 0, r = n;
    while (l < r - 1) {
      LL mid = (l + r) >> 1;
      LL tnum = cal(mid);
      if (tnum < num) {
        l = mid;
      } else {
        r = mid;
      }
    }
    printf("Case #%d: %I64d\n", t, r);
  }
  return 0;
}
