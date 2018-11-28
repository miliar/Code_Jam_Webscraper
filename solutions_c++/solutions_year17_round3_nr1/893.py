#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX = 1005;
const long long INF = 2000111000111000;

pair<int, int> pancake[MAX];
long long dp[MAX][MAX];
long long H[MAX], R[MAX], LPH[MAX];
int n, x;

long long f(int i, int k) {

  if(!k) return 0;
  else if(i == n) return -INF;

  long long &ret = dp[i][k];
  if(ret != -INF) return ret;

  ret = std::max(ret, f(i+1, k));
  ret = std::max(ret, f(i+1,k-1)+ LPH[i]);

  // printf("DP %d %d: %.7lf\n", i, k, ret);
  return ret;
}

bool cmp(const pair<int,int> &a, const pair<int,int> &b) {
  return a.first > b.first;
}

int main() {
  int T; scanf("%d", &T);
  for(int tc = 1;tc <= T;++tc) {
    printf("Case #%d: ", tc);
    scanf("%d%d", &n, &x);
    for(int i = 0;i < n;++i) scanf("%d%d", &pancake[i].first, &pancake[i].second);

    sort(pancake, pancake+n, cmp);
    for(int i = 0;i < n;++i) {
      R[i] = pancake[i].first;
      H[i] = pancake[i].second;
      LPH[i] = 2 * R[i] * H[i];
      for(int j = 0;j < n;++j) dp[i][j] = -INF;
    }

    long long ans = 0;
    for(int i = 0;i < n;++i) {
      long long now = f(i+1, x-1) + (1LL * R[i] * R[i]) + (2LL * R[i] * H[i]);
      // printf("ANS %d: %lld\n", i, now);
      ans = std::max(ans, now);
    }

    // printf("ANS = %lld\n", ans);
    printf("%.10lf\n", ans * M_PI);
  }
}
