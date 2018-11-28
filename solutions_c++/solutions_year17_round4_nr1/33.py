#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
typedef int64_t i64;

i64 DP[110][110][110][4];

i64 recur(i64 P, i64 c1, i64 c2, i64 c3, i64 rem) {
  if (c1 == 0 && c2 == 0 && c3 == 0) {
    return 0;
  }
  if (DP[c1][c2][c3][rem] != -1) {
    return DP[c1][c2][c3][rem];
  }
  i64 ans = 0;
  i64 start = rem == 0 ? 1 : 0;
  if (c1 > 0) {
    ans = max(ans, start + recur(P, c1-1, c2, c3, (rem + 1) % P));
  }
  if (c2 > 0) {
    ans = max(ans, start + recur(P, c1, c2-1, c3, (rem + 2) % P));
  }
  if (c3 > 0) {
    ans = max(ans, start + recur(P, c1, c2, c3-1, (rem + 3) % P));
  }
  //printf("%lld %lld %lld %lld %lld\n", c1, c2, c3, rem, ans);
  DP[c1][c2][c3][rem] = ans;
  return ans;
}

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    i64 N, P;
    scanf("%lld %lld", &N, &P);
    vector<i64> C(4);
    for (i64 i = 0; i < N; i++) {
      i64 v;
      scanf("%lld", &v);
      C[v % P]++;
    }
    memset(DP, -1, sizeof(DP));
    i64 ans = C[0];
    ans += recur(P, C[1], C[2], C[3], 0);

    printf("Case #%lld: %lld\n", zz, ans);
  }
}
