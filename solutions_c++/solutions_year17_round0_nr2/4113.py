#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[22];
int len;
long long p[22];
long long dp[22][11][2][2];

long long solve(int a, int b, int c, int z) {
  // printf("%d %d %d %d\n", a, b, c, z);
  if (!s[a]) {
    return 1-z;
  }
  if (dp[a][b][c][z] >= 0) return dp[a][b][c][z];
  long long res = 0;
  int lim = (c ? s[a]-'0' : 9);
  for (int i = 0; i <= lim; i++) {
    if (z || b <= i) {
      long long ret = solve(a+1, i, c && i == lim, z && i == 0);
      if (ret > 0) {
        res = max(res, i*p[len-1-a] + (s[a+1] ? ret : 0));
      }
    }
  }
  return dp[a][b][c][z] = res;
}

int main(void) {
  int T; scanf("%d", &T);
  p[0] = 1;
  for (int i = 0; i < 22; i++) p[i+1] = p[i]*10;
  for (int ijk = 1; ijk <= T; ijk++) {
    scanf("%s", s); len = strlen(s);
    memset(dp, -1, sizeof(dp));
    long long res = solve(0, 0, 1, 1);
    printf("Case #%d: %lld\n", ijk, res);
  }
  return 0;
}
