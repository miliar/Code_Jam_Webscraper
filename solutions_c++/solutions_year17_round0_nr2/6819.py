#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long ll;

int T, n;
ll dp[30][10][2], M[30];
char A[30];

const ll INF = 2000000000000000000;

ll func(int pos, int last, int flag) {
  if (pos == n) {
    return 0;
  }

  ll& ret = dp[pos][last][flag];
  if (ret != -INF) {
    return ret;
  }

  bool next = false;
  if (flag) {
    for (int i = last ; i < 10 ; ++i) {
      next = true;
      ret = max(ret, func(pos + 1, i, flag) + i * M[pos]);
    }
  } else {
    int limit = A[pos] - '0';
    for (int i = last ; i <= limit ; ++i) {
      next = true;
      ret = max(ret, func(pos + 1, i, i == limit ? 0 : 1) + i * M[pos]);
    }
  }

  return next ? ret : -INF * 2;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; ++t) {
    scanf("%s", A);
    n = strlen(A);
    M[n - 1] = 1;
    for (int i = n - 2 ; i >= 0 ; --i) {
      M[i] = M[i + 1] * 10LL;
    }

    for (int i = 0 ; i < 30 ; ++i) {
      for (int j = 0 ; j < 10 ; ++j) {
        dp[i][j][0] = dp[i][j][1] = -INF;
      }
    }

    int limit = A[0] - '0';
    ll ans = 0;
    for (int i = 0 ; i <= limit ; ++i) {
      ans = max(ans, func(1, i, i == limit ? 0 : 1) + i * M[0]);
    }

    printf("Case #%d: %lld\n", t, ans);
  }
}